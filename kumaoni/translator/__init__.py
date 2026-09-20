"""
Translation module for Kumaoni language.
"""

from kumaoni.translator.engine import (
    Translator,
    TranslationResult,
    translate,
)
from kumaoni.translator.rule_based import RuleBasedTranslator
from kumaoni.translator.pivot import PivotTranslator
from kumaoni.translator.llm_adapter import LLMTranslator

__all__ = [
    "Translator",
    "TranslationResult",
    "translate",
    "RuleBasedTranslator",
    "PivotTranslator",
    "LLMTranslator",
]
