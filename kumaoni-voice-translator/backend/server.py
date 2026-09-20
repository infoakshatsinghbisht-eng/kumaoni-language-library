# -*- coding: utf-8 -*-
"""
Kumaoni Voice Translator - FastAPI Backend Server.
Provides high-performance REST and streaming APIs for voice translation,
speech phonetics analysis, SSML generation, and PCM WAV audio synthesis.
"""

import sys
from pathlib import Path

# Ensure kumaoni library is discoverable
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIB_ROOT = PROJECT_ROOT.parent
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

from typing import Optional, List, Dict, Any
from fastapi import FastAPI, Query, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

try:
    import kumaoni
    from kumaoni.voice import KumaoniVoiceSynthesizer, voice_translate
except ImportError as e:
    raise RuntimeError(f"Failed to import kumaoni package: {e}")


app = FastAPI(
    title="Kumaoni Voice Translator API",
    description="Official REST & Voice Synthesis API for Kumaoni Language Translation",
    version="1.0.0",
)

# Enable CORS for local Vite dev server and production frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VoiceTranslateRequest(BaseModel):
    text: str = Field(..., description="Source text or spoken transcript to translate")
    source_lang: str = Field("auto", description="Source language code (e.g., 'en', 'hi', 'fr', 'auto')")
    target_dialect: str = Field("central", description="Kumaoni dialect ('central', 'eastern', 'western')")
    method: str = Field("auto", description="Translation engine ('auto', 'rule_based', 'pivot', 'llm')")
    generate_audio: bool = Field(True, description="Whether to include base64 audio and pitch envelope")
    api_key: Optional[str] = Field(None, description="Optional LLM API key for neural mode")


class VoiceTranslateResponse(BaseModel):
    source_text: str
    source_lang: str
    translated_text: str
    romanized: str
    phonetic_script: Dict[str, Any]
    syllables: List[str]
    ssml: str
    audio_wav_base64: Optional[str] = None
    confidence: float
    category: Optional[str] = None
    method: str


class DialogueExchangeRequest(BaseModel):
    speaker: str = Field("person_a", description="'person_a' (Tourist/Visitor) or 'person_b' (Local Resident)")
    message: str = Field(..., description="Spoken message")
    source_lang: str = Field("en", description="Language of speaker")


@app.get("/api/health")
def health_check():
    """Service health and engine version check."""
    return {
        "status": "healthy",
        "service": "kumaoni-voice-translator",
        "version": "1.0.0",
        "library_version": getattr(kumaoni, "__version__", "1.0.0"),
        "total_morph_words": kumaoni.total_word_forms() if hasattr(kumaoni, "total_word_forms") else 300516,
    }


@app.post("/api/voice/translate", response_model=VoiceTranslateResponse)
def translate_voice(req: VoiceTranslateRequest):
    """
    Main Voice Translation endpoint.
    Translates input text into authentic Kumaoni with syllabic stress breakdown and SSML.
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    res = voice_translate(
        text=req.text,
        source_lang=req.source_lang,
        method=req.method,
        generate_audio=req.generate_audio,
        api_key=req.api_key,
    )
    return res.to_dict()


@app.post("/api/voice/dialogue")
def handle_dialogue_exchange(req: DialogueExchangeRequest):
    """
    Two-way dialogue helper for conversations between a visitor and a Kumaoni native.
    """
    if req.speaker == "person_a":
        # Visitor speaking in English/Hindi -> Translate to Kumaoni
        res = voice_translate(req.message, source_lang=req.source_lang, generate_audio=True)
        return {
            "speaker": req.speaker,
            "original": req.message,
            "translated_kumaoni": res.translated_text,
            "romanized": res.romanized,
            "syllables": res.syllables,
            "audio_wav_base64": res.audio_wav_base64,
            "direction": "visitor_to_local"
        }
    else:
        # Local speaking in Kumaoni -> Translate back to visitor's language
        # For Kumaoni -> English/Hindi translation
        res_tr = kumaoni.translate(req.message, source="kmy")
        return {
            "speaker": req.speaker,
            "original": req.message,
            "translated_kumaoni": req.message,
            "translated_english": res_tr.text,
            "romanized": kumaoni.devanagari_to_latin(req.message),
            "direction": "local_to_visitor"
        }


@app.get("/api/voice/phrases")
def get_spoken_phrases(category: str = Query("all", description="Category filter")):
    """Returns curated mountain voice dialogue phrases."""
    phrases = kumaoni.voice.phrases(category=category)
    return {"category": category, "count": len(phrases), "phrases": phrases}


@app.get("/api/voice/wav")
def get_synthesized_wav(
    duration: float = Query(0.6, description="Duration in seconds"),
    freq: float = Query(440.0, description="Base frequency in Hz")
):
    """Generates raw uncompressed PCM WAV audio stream."""
    wav_bytes = KumaoniVoiceSynthesizer.generate_pcm_wav(duration_seconds=duration, freq=freq)
    return Response(content=wav_bytes, media_type="audio/wav")


if __name__ == "__main__":
    import uvicorn
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Starting Kumaoni Voice Translator Backend on http://localhost:{port}")
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
