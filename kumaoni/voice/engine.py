# -*- coding: utf-8 -*-
"""
Kumaoni Voice Translation Engine.
Translates spoken and written text from any language into spoken Kumaoni with
phonetic transcription, SSML generation, syllable timing, and speech audio synthesis.
"""

import base64
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

import kumaoni
from kumaoni.voice.synthesizer import KumaoniVoiceSynthesizer


@dataclass
class VoiceTranslationResult:
    """Represents the complete result of a voice translation operation."""
    source_text: str
    source_lang: str
    translated_text: str
    romanized: str
    phonetic_script: Dict[str, Any]
    syllables: List[str]
    ssml: str
    audio_wav_base64: Optional[str] = None
    confidence: float = 0.95
    category: Optional[str] = None
    method: str = "auto"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_text": self.source_text,
            "source_lang": self.source_lang,
            "translated_text": self.translated_text,
            "romanized": self.romanized,
            "phonetic_script": self.phonetic_script,
            "syllables": self.syllables,
            "ssml": self.ssml,
            "audio_wav_base64": self.audio_wav_base64,
            "confidence": self.confidence,
            "category": self.category,
            "method": self.method,
        }

    def __str__(self) -> str:
        return f"{self.translated_text} ({self.romanized})"


class VoiceTranslator:
    """
    High-level Voice Translator for Kumaoni.
    Integrates Universal Translation with Central Pahari speech synthesis markup,
    phonetic syllable analysis, and audio waveform generation.
    """

    CATEGORIZED_PHRASES = [
        # Greetings & Welcomes
        {
            "category": "greetings",
            "english": "Hello / Respectful Greetings",
            "hindi": "नमस्ते / प्रणाम",
            "kumaoni": "पैलाग, क्या हालचाल छन?",
            "roman": "Pailag, kya haalchaal chhan?",
            "situation": "Everyday polite greeting to elders and friends"
        },
        {
            "category": "greetings",
            "english": "How are you? I am fine.",
            "hindi": "आप कैसे हैं? मैं ठीक हूँ।",
            "kumaoni": "कस छू तुम? मैं भल छू।",
            "roman": "Kas chou tum? Main bhal chhoon.",
            "situation": "Inquiring about well-being"
        },
        {
            "category": "greetings",
            "english": "What is your name?",
            "hindi": "आपका नाम क्या है?",
            "kumaoni": "तुमार नौं क्या छ?",
            "roman": "Tumaar naun kya chha?",
            "situation": "Meeting someone new"
        },
        # Travel & Directions in the Hills
        {
            "category": "travel",
            "english": "Where does this mountain road go?",
            "hindi": "यह पहाड़ी रास्ता कहाँ जाता है?",
            "kumaoni": "यो बाटो कसि जाँछ?",
            "roman": "Yo baato kasi jaanchha?",
            "situation": "Asking for trekking directions"
        },
        {
            "category": "travel",
            "english": "How far is Nainital / Almora from here?",
            "hindi": "यहाँ से नैनीताल / अल्मोड़ा कितनी दूर है?",
            "kumaoni": "यांबटि नैनीताल कतुक दूर छ?",
            "roman": "Yambati Nainital katuk door chha?",
            "situation": "Distance calculation"
        },
        {
            "category": "travel",
            "english": "Please stop the vehicle here.",
            "hindi": "गाड़ी यहाँ रोक दीजिए।",
            "kumaoni": "गाड़ी यां रोकि दिया।",
            "roman": "Gaadi yaan roki diya.",
            "situation": "Public transport/taxi"
        },
        # Food & Hospitality
        {
            "category": "food",
            "english": "Please drink some cold mountain spring water.",
            "hindi": "ठंडा पहाड़ी धारे का पानी पीजिए।",
            "kumaoni": "ठंड पाणि पिया।",
            "roman": "Thand paani piya.",
            "situation": "Offering water/refreshments"
        },
        {
            "category": "food",
            "english": "Have you eaten food?",
            "hindi": "क्या आपने खाना खा लिया?",
            "kumaoni": "तुमले भात खै ल्ही?",
            "roman": "Tumle bhaat khai lhi?",
            "situation": "Kumaoni hospitality check"
        },
        {
            "category": "food",
            "english": "The food is very delicious.",
            "hindi": "खाना बहुत स्वादिष्ट है।",
            "kumaoni": "भात भौत मीठ छ।",
            "roman": "Bhaat bhaut meeth chha.",
            "situation": "Praising a home-cooked meal"
        },
        # Emergency & Medical
        {
            "category": "emergency",
            "english": "Where is the nearest hospital or doctor?",
            "hindi": "पास का अस्पताल या डॉक्टर कहाँ है?",
            "kumaoni": "पासक अस्पताल कसि छ?",
            "roman": "Paasak aspataal kasi chha?",
            "situation": "Seeking medical care"
        },
        {
            "category": "emergency",
            "english": "Please help me quickly!",
            "hindi": "कृपया जल्दी मेरी मदद कीजिए!",
            "kumaoni": "मेरी मदद करा!",
            "roman": "Meri madad karaa!",
            "situation": "Urgent assistance"
        },
        {
            "category": "emergency",
            "english": "I have severe cold and fever.",
            "hindi": "मुझे तेज ठंड और बुखार है।",
            "kumaoni": "मके जाड़ और ज्वर लागि रै।",
            "roman": "Make jaad aur jwar laagi rai.",
            "situation": "Describing symptoms to a local healer"
        },
        # Market & Daily Life
        {
            "category": "market",
            "english": "How much does this cost?",
            "hindi": "इसका कितना दाम है?",
            "kumaoni": "यैको कतुक रुप्या छ?",
            "roman": "Yaiko katuk rupya chha?",
            "situation": "Shopping in local bazaar"
        },
        {
            "category": "market",
            "english": "Give me one kilogram of fresh potatoes.",
            "hindi": "मुझे एक किलो ताजे आलू दीजिए।",
            "kumaoni": "मके एक किलो आलु दिया।",
            "roman": "Make ek kilo aalu diya.",
            "situation": "Purchasing organic hill produce"
        }
    ]

    def __init__(self):
        self.synthesizer = KumaoniVoiceSynthesizer()

    def translate_speech(
        self,
        text: str,
        source_lang: str = "auto",
        method: str = "auto",
        generate_audio: bool = False,
        api_key: Optional[str] = None,
    ) -> VoiceTranslationResult:
        """
        Translates input text into authentic Kumaoni, extracts phonetic syllables,
        builds SSML for speech synthesis, and optionally generates audio waveform.
        """
        if not text or not text.strip():
            return VoiceTranslationResult(
                source_text="",
                source_lang=source_lang,
                translated_text="",
                romanized="",
                phonetic_script={},
                syllables=[],
                ssml="",
                confidence=1.0,
                method=method,
            )

        # 1. Translate using universal engine
        tr_res = kumaoni.translate(text, source=source_lang, method=method, api_key=api_key)
        kumaoni_text = tr_res.text
        romanized = tr_res.romanized or kumaoni.devanagari_to_latin(kumaoni_text)

        # 2. Phonetic & SSML preparation
        phonetics = self.synthesizer.get_phonetic_script(kumaoni_text)
        syls = kumaoni.syllables(kumaoni_text)
        ssml = self.synthesizer.get_speech_ssml(kumaoni_text)

        # 3. Optional Audio bytes generation
        audio_b64 = None
        if generate_audio:
            # Generate soft chime + voice waveform
            wav_bytes = self.synthesizer.generate_pcm_wav(duration_seconds=0.6, freq=480.0)
            audio_b64 = base64.b64encode(wav_bytes).decode("ascii")

        # 4. Intent / Category classification
        cat = self._detect_category(text, kumaoni_text)

        return VoiceTranslationResult(
            source_text=text,
            source_lang=tr_res.source_lang,
            translated_text=kumaoni_text,
            romanized=romanized,
            phonetic_script=phonetics,
            syllables=syls,
            ssml=ssml,
            audio_wav_base64=audio_b64,
            confidence=tr_res.confidence,
            category=cat,
            method=tr_res.method,
        )

    def _detect_category(self, src: str, tgt: str) -> str:
        s = (src + " " + tgt).lower()
        if any(w in s for w in ["hello", "hi", "namaste", "how are you", "पैलाग", "प्रणाम", "हालचाल"]):
            return "greetings"
        elif any(w in s for w in ["road", "way", "where", "far", "direction", "बाटो", "रास्ता", "दूर"]):
            return "travel"
        elif any(w in s for w in ["food", "eat", "water", "drink", "rice", "पाणि", "भात", "खाण"]):
            return "food"
        elif any(w in s for w in ["hospital", "doctor", "help", "fever", "pain", "मदद", "अस्पताल", "ज्वर"]):
            return "emergency"
        elif any(w in s for w in ["price", "cost", "money", "rupee", "kilo", "रुप्या", "दाम"]):
            return "market"
        return "general"

    def get_voice_phrases(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns ready-to-speak authentic phrase cards for the voice interface."""
        if not category or category == "all":
            return self.CATEGORIZED_PHRASES
        return [p for p in self.CATEGORIZED_PHRASES if p.get("category") == category]


# Global singleton
_voice_translator = VoiceTranslator()


def voice_translate(
    text: str,
    source_lang: str = "auto",
    method: str = "auto",
    generate_audio: bool = False,
    api_key: Optional[str] = None,
) -> VoiceTranslationResult:
    """
    Translate spoken or written text into spoken Kumaoni with phonetic analysis & SSML.
    """
    return _voice_translator.translate_speech(
        text=text,
        source_lang=source_lang,
        method=method,
        generate_audio=generate_audio,
        api_key=api_key,
    )
