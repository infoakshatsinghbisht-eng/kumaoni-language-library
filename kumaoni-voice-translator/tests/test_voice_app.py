# -*- coding: utf-8 -*-
"""
Test suite for the Kumaoni Voice Translator Web App & FastAPI Backend.
Supports both direct router inspection and TestClient.
"""

import sys
from pathlib import Path
import unittest

PROJECT_DIR = Path(__file__).resolve().parent.parent
LIB_DIR = PROJECT_DIR.parent
sys.path.insert(0, str(PROJECT_DIR))
sys.path.insert(0, str(LIB_DIR))

from backend.server import (
    app,
    health_check,
    translate_voice,
    handle_dialogue_exchange,
    get_spoken_phrases,
    get_synthesized_wav,
    VoiceTranslateRequest,
    DialogueExchangeRequest,
)


class TestVoiceAppAPI(unittest.TestCase):

    def test_health_check(self):
        data = health_check()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "kumaoni-voice-translator")

    def test_voice_translate_endpoint(self):
        req = VoiceTranslateRequest(
            text="Where is the hospital?",
            source_lang="en",
            target_dialect="central",
            method="auto",
            generate_audio=True,
        )
        data = translate_voice(req)
        self.assertIn("translated_text", data)
        self.assertTrue(len(data["translated_text"]) > 0)
        self.assertIn("romanized", data)
        self.assertIn("syllables", data)
        self.assertIn("ssml", data)
        self.assertIsNotNone(data.get("audio_wav_base64"))

    def test_dialogue_visitor(self):
        req = DialogueExchangeRequest(
            speaker="person_a",
            message="Where is the river?",
            source_lang="en",
        )
        data = handle_dialogue_exchange(req)
        self.assertEqual(data["direction"], "visitor_to_local")
        self.assertIn("translated_kumaoni", data)

    def test_dialogue_native(self):
        req = DialogueExchangeRequest(
            speaker="person_b",
            message="यो पाणि मीठ छ।",
            source_lang="kmy",
        )
        data = handle_dialogue_exchange(req)
        self.assertEqual(data["direction"], "local_to_visitor")

    def test_voice_phrases(self):
        data = get_spoken_phrases(category="travel")
        self.assertEqual(data["category"], "travel")
        self.assertTrue(len(data["phrases"]) > 0)

    def test_voice_wav_stream(self):
        resp = get_synthesized_wav(duration=0.2, freq=440.0)
        self.assertEqual(resp.media_type, "audio/wav")
        self.assertTrue(resp.body.startswith(b"RIFF"))


if __name__ == "__main__":
    unittest.main()
