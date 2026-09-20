"""
LLM adapter for state-of-the-art neural Kumaoni translation.
Supports Google Gemini API, OpenAI, and custom LLM providers.
Requires zero external pip packages by utilizing standard library HTTP requests.
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Optional, Dict, Any, Tuple


KUMAONI_SYSTEM_PROMPT = """You are an expert native linguist and translator for the Kumaoni language (कुमाऊँनी), an Indo-Aryan Central Pahari language spoken in the Kumaon region of Uttarakhand, India.

Your task is to translate sentences from ANY source language into authentic, natural Kumaoni.

Key Linguistic Rules for Kumaoni:
1. Script: Write the translation primarily in Devanagari (कुमाऊँनी).
2. Sentence Structure: Follow strict SOV (Subject - Object - Verb) word order.
3. Substantive Verb 'to be':
   - Present: छूँ (I am), छे (you are-informal), छौ (you are-respectful), छ (he/she is), छां (we are), छन (they are).
   - Past: थ्यूँ (I was), थो (he was), थी (she was), था (they were).
4. Case Markers / Postpositions:
   - Agentive/Ergative: -ले (e.g. रामले)
   - Accusative/Dative: -कणी / -कण (e.g. मैंकणी)
   - Ablative: -बटि / -हैं (e.g. घरबटि)
   - Locative: -म / -पं (e.g. गाँवम)
   - Genitive: -को, -की, -का
5. Common Vocabulary:
   - Greetings: पैलाग (elder), नमस्कार / जय देव
   - Kinship: ईजा (mother), बाबु (father), दाज्यू (elder brother), भुली (younger sister), दीदी (elder sister), बूबू (grandfather), आमा (grandmother)
   - Food/Everyday: पाणि (water), भात (cooked rice/food), घाम (sunshine), जाड़ (cold), भाल (good)

Respond with valid JSON in this exact format:
{
  "translation": "<Devanagari Kumaoni text>",
  "romanized": "<Phonetic Latin transliteration>",
  "explanation": "<Brief grammatical note if helpful>"
}
"""


class LLMTranslator:
    def __init__(
        self,
        provider: str = "gemini",
        api_key: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.provider = provider.lower()
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.model = model

    def is_available(self) -> bool:
        """Check if an API key is configured."""
        return bool(self.api_key)

    def translate(
        self,
        text: str,
        source_lang: str = "auto",
        dialect: str = "standard"
    ) -> Optional[Tuple[str, str]]:
        """
        Translates text to Kumaoni using configured LLM.
        Returns: (kumaoni_devanagari, romanized) or None if request fails.
        """
        if not self.is_available():
            return None

        prompt = f"Translate the following text from {source_lang} into {dialect} dialect Kumaoni:\n\nText: {text}"

        if "gemini" in self.provider or os.environ.get("GEMINI_API_KEY"):
            return self._call_gemini(prompt)
        elif "openai" in self.provider or os.environ.get("OPENAI_API_KEY"):
            return self._call_openai(prompt)
            
        return None

    def _call_gemini(self, user_prompt: str) -> Optional[Tuple[str, str]]:
        """Call Gemini API via standard library HTTPS."""
        model = self.model or "gemini-2.5-flash"
        api_key = self.api_key or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return None

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{KUMAONI_SYSTEM_PROMPT}\n\n{user_prompt}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=10.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text_content = data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = json.loads(text_content)
                return parsed.get("translation", ""), parsed.get("romanized", "")
        except Exception:
            return None

    def _call_openai(self, user_prompt: str) -> Optional[Tuple[str, str]]:
        """Call OpenAI API via standard library HTTPS."""
        model = self.model or "gpt-4o-mini"
        api_key = self.api_key or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return None

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": KUMAONI_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.2
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=10.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                content = data["choices"][0]["message"]["content"]
                parsed = json.loads(content)
                return parsed.get("translation", ""), parsed.get("romanized", "")
        except Exception:
            return None
