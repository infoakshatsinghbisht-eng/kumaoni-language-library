"""
Unified translation engine for Kumaoni.
Coordinates rule-based parsing, universal world-language pivot bridging, and neural LLM adapters.
"""

from dataclasses import dataclass
from typing import Optional, Union
from kumaoni.translator.rule_based import RuleBasedTranslator
from kumaoni.translator.pivot import PivotTranslator
from kumaoni.translator.llm_adapter import LLMTranslator
from kumaoni.phonetics import devanagari_to_latin


@dataclass
class TranslationResult:
    text: str                       # Kumaoni Devanagari translation
    romanized: str                  # Phonetic Latin/English transliteration
    source: str                     # Original input text
    source_lang: str                # Source language code
    target_lang: str = "kmy"        # Target language (Kumaoni)
    method: str = "auto"            # "rule_based", "pivot", "llm"
    confidence: float = 1.0

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"<TranslationResult text='{self.text}' romanized='{self.romanized}' method='{self.method}'>"


class Translator:
    def __init__(self):
        self.rule_based = RuleBasedTranslator()
        self.pivot = PivotTranslator()
        self.llm = LLMTranslator()

    def translate(
        self,
        text: str,
        source: str = "auto",
        target: str = "kmy",
        dialect: str = "standard",
        method: str = "auto",
        api_key: Optional[str] = None
    ) -> TranslationResult:
        """
        Translates text from ANY language into Kumaoni.
        
        Args:
            text: The text to translate.
            source: Source language code (e.g., 'en', 'hi', 'fr', 'es', 'de', 'ja', 'auto').
            target: Target language code (default 'kmy' for Kumaoni).
            dialect: Preferred Kumaoni dialect (e.g., 'standard', 'soryali', 'gangoli').
            method: 'auto', 'rule_based', 'pivot', or 'llm'.
            api_key: Optional Gemini or OpenAI API key for neural translation.
        """
        clean_text = text.strip()
        if not clean_text:
            return TranslationResult(
                text="",
                romanized="",
                source=text,
                source_lang=source,
                method="none",
                confidence=0.0
            )

        # 1. LLM Translation requested or available with explicit key
        if method == "llm" or (api_key and method == "auto"):
            custom_llm = LLMTranslator(api_key=api_key) if api_key else self.llm
            if custom_llm.is_available():
                res = custom_llm.translate(clean_text, source_lang=source, dialect=dialect)
                if res and res[0]:
                    dev, rom = res
                    return TranslationResult(
                        text=dev,
                        romanized=rom or devanagari_to_latin(dev),
                        source=clean_text,
                        source_lang=source,
                        method="llm",
                        confidence=0.98
                    )

        # Normalize source language code
        src = source.lower().strip()
        if src in ("auto", ""):
            # Simple heuristic
            has_dev = any('\u0900' <= c <= '\u097F' for c in clean_text)
            src = "hi" if has_dev else "en"

        # 2. Rule-based translation (if source is English or Hindi)
        if src in ("en", "eng", "english") and method in ("auto", "rule_based"):
            kmy, conf = self.rule_based.translate_en_to_kmy(clean_text)
            return TranslationResult(
                text=kmy,
                romanized=devanagari_to_latin(kmy),
                source=clean_text,
                source_lang="en",
                method="rule_based",
                confidence=conf
            )
        elif src in ("hi", "hin", "hindi") and method in ("auto", "rule_based"):
            kmy, conf = self.rule_based.translate_hi_to_kmy(clean_text)
            return TranslationResult(
                text=kmy,
                romanized=devanagari_to_latin(kmy),
                source=clean_text,
                source_lang="hi",
                method="rule_based",
                confidence=conf
            )

        # 3. Universal Multi-Language Pivot Bridging (French, Spanish, German, Japanese, etc.)
        kmy, pivot_en, conf = self.pivot.translate_to_kumaoni(clean_text, source_lang=src)
        return TranslationResult(
            text=kmy,
            romanized=devanagari_to_latin(kmy),
            source=clean_text,
            source_lang=src,
            method="pivot",
            confidence=conf
        )


# Global instance for quick top-level calls
_global_translator = Translator()


def translate(
    text: str,
    source: str = "auto",
    target: str = "kmy",
    dialect: str = "standard",
    method: str = "auto",
    api_key: Optional[str] = None
) -> TranslationResult:
    """
    Main entry point for Kumaoni translation.
    E.g.:
    >>> translate("How are you?")
    <TranslationResult text='कस छू तुम?' romanized='kas chhoo tum?'>
    >>> translate("Comment allez-vous?", source="fr")
    <TranslationResult text='कस छू तुम?' romanized='kas chhoo tum?'>
    """
    return _global_translator.translate(
        text=text,
        source=source,
        target=target,
        dialect=dialect,
        method=method,
        api_key=api_key
    )
