"""
Universal Multi-Language Pivot Translator:
Translates from ANY world language (French, Spanish, German, Japanese, Russian, Arabic, etc.)
into Kumaoni by bridging through English/Hindi with zero required API keys.
"""

import urllib.request
import urllib.parse
import json
from typing import Tuple, Optional
from kumaoni.translator.rule_based import RuleBasedTranslator


class PivotTranslator:
    def __init__(self):
        self.rule_translator = RuleBasedTranslator()
        self._cache = {}

    def translate_to_kumaoni(
        self,
        text: str,
        source_lang: str = "auto",
        timeout_seconds: float = 4.0
    ) -> Tuple[str, str, float]:
        """
        Translates text from any world language to Kumaoni.
        Returns: (kumaoni_translation, intermediate_english, confidence)
        """
        text = text.strip()
        if not text:
            return "", "", 0.0

        src_clean = source_lang.lower().strip()
        cache_key = (text, src_clean)
        if cache_key in self._cache:
            return self._cache[cache_key]

        # 1. If already English
        if src_clean in ("en", "eng", "english"):
            kmy, conf = self.rule_translator.translate_en_to_kmy(text)
            res = (kmy, text, conf)
            self._cache[cache_key] = res
            return res

        # 2. If Hindi
        if src_clean in ("hi", "hin", "hindi"):
            kmy, conf = self.rule_translator.translate_hi_to_kmy(text)
            res = (kmy, text, conf)
            self._cache[cache_key] = res
            return res

        # 3. Any other world language -> Pivot via English
        intermediate_en = self._pivot_to_english(text, src_clean, timeout=timeout_seconds)
        if intermediate_en:
            kmy, conf = self.rule_translator.translate_en_to_kmy(intermediate_en)
            res = (kmy, intermediate_en, conf * 0.9)
            self._cache[cache_key] = res
            return res

        # Fallback if offline or pivot failed
        kmy, conf = self.rule_translator.translate_en_to_kmy(text)
        return kmy, text, conf * 0.5

    def _pivot_to_english(self, text: str, source_lang: str, timeout: float = 4.0) -> Optional[str]:
        """
        Translates text from source_lang to English using free public translation APIs.
        Includes timeout protection and fallback.
        """
        # Attempt 1: MyMemory public API
        try:
            langpair = f"{source_lang}|en" if source_lang != "auto" else "autodetect|en"
            url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair={langpair}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Kumaoni-Language-Library)"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    matches = data.get("responseData", {})
                    translated = matches.get("translatedText")
                    if translated and not translated.startswith("MYMEMORY WARNING"):
                        return translated
        except Exception:
            pass

        # Attempt 2: Lingva public bridge
        try:
            url = f"https://lingva.ml/api/v1/{source_lang}/en/{urllib.parse.quote(text)}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Kumaoni-Language-Library)"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    trans = data.get("translation")
                    if trans:
                        return trans
        except Exception:
            pass

        return None
