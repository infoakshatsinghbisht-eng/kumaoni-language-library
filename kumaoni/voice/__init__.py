# -*- coding: utf-8 -*-
"""
Kumaoni Voice, Speech Recognition & Speech Synthesis Subsystem.
"""

from kumaoni.voice.synthesizer import KumaoniVoiceSynthesizer
from kumaoni.voice.engine import (
    VoiceTranslator,
    VoiceTranslationResult,
    voice_translate,
)

__all__ = [
    "KumaoniVoiceSynthesizer",
    "VoiceTranslator",
    "VoiceTranslationResult",
    "voice_translate",
]
