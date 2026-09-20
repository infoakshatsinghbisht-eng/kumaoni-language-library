# -*- coding: utf-8 -*-
"""
Unit tests for the Kumaoni Voice and Speech Synthesis engine.
"""

import unittest
import kumaoni
from kumaoni.voice import KumaoniVoiceSynthesizer, VoiceTranslator, voice_translate


class TestVoice(unittest.TestCase):

    def test_voice_translate_english(self):
        res = voice_translate("How are you?", source_lang="en")
        self.assertIsNotNone(res)
        self.assertTrue(len(res.translated_text) > 0)
        self.assertTrue(len(res.romanized) > 0)
        self.assertTrue(len(res.syllables) > 0)
        self.assertIn("<speak>", res.ssml)
        self.assertEqual(res.category, "greetings")

    def test_voice_translate_hindi(self):
        res = kumaoni.voice.translate("आप कहाँ रहते हैं?", source_lang="hi")
        self.assertIsNotNone(res)
        self.assertTrue(len(res.translated_text) > 0)
        self.assertIn("तुम", res.translated_text)

    def test_voice_synthesizer_ssml(self):
        ssml = KumaoniVoiceSynthesizer.get_speech_ssml("तुम कस छू?")
        self.assertIn("<speak>", ssml)
        self.assertIn("</speak>", ssml)

    def test_voice_synthesizer_pcm_wav(self):
        wav = KumaoniVoiceSynthesizer.generate_pcm_wav(duration_seconds=0.2, freq=440.0)
        self.assertTrue(wav.startswith(b"RIFF"))
        self.assertIn(b"WAVE", wav)
        self.assertIn(b"fmt ", wav)
        self.assertIn(b"data", wav)

    def test_voice_phrases(self):
        phrases = kumaoni.voice.phrases(category="greetings")
        self.assertTrue(len(phrases) >= 3)
        p0 = phrases[0]
        self.assertIn("kumaoni", p0)
        self.assertIn("english", p0)
        self.assertIn("roman", p0)

    def test_voice_facade(self):
        res = kumaoni.voice.translate("Hello", source_lang="en", generate_audio=True)
        self.assertIsNotNone(res.audio_wav_base64)
        self.assertTrue(len(res.audio_wav_base64) > 0)


if __name__ == "__main__":
    unittest.main()
