"""
Kumaoni lexicon and dictionary lookup engine.
Supports fast searching across Devanagari, Latin/Romanized transliterations, English, and Hindi.
"""

import json
import random
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

DATA_DIR = Path(__file__).parent / "data"


import re

STOPWORDS_EN = {
    "a", "an", "the", "and", "or", "of", "in", "on", "at", "to", "for", "with", "by", "from",
    "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", "does", "did",
    "it", "its", "this", "that", "these", "those", "like", "such", "as", "about", "into", "through",
    "after", "before", "between", "under", "over", "above", "below", "some", "any", "which", "who",
    "whom", "whose", "where", "when", "why", "how", "all", "both", "each", "few", "more", "most",
    "other", "same", "so", "than", "too", "very", "can", "will", "just", "should", "now"
}


@dataclass
class Word:
    kumaoni: str
    roman: str
    english: str
    hindi: str
    pos: str
    category: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class Lexicon:
    _instance: Optional["Lexicon"] = None

    def __init__(self):
        self._words: List[Word] = []
        self._kumaoni_map: Dict[str, Word] = {}
        self._roman_map: Dict[str, Word] = {}
        self._english_exact_map: Dict[str, Word] = {}
        self._english_map: Dict[str, List[Word]] = {}
        self._hindi_exact_map: Dict[str, Word] = {}
        self._hindi_map: Dict[str, List[Word]] = {}
        self._phrases: List[Dict[str, Any]] = []
        self._proverbs: List[Dict[str, Any]] = []
        self._riddles: List[Dict[str, Any]] = []
        
        self._load_data()

    @classmethod
    def get_instance(cls) -> "Lexicon":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_data(self):
        # Load words
        words_path = DATA_DIR / "words.json"
        if words_path.exists():
            with open(words_path, "r", encoding="utf-8") as f:
                raw_words = json.load(f)
                for item in raw_words:
                    word = Word(
                        kumaoni=item["kumaoni"],
                        roman=item["roman"],
                        english=item["english"],
                        hindi=item["hindi"],
                        pos=item.get("pos", "noun"),
                        category=item.get("category", "general"),
                    )
                    self._words.append(word)

                    # Preserve primary canonical entry if already exists
                    if word.kumaoni not in self._kumaoni_map:
                        self._kumaoni_map[word.kumaoni] = word

                    rom_key = word.roman.lower().strip()
                    if rom_key and rom_key not in self._roman_map:
                        self._roman_map[rom_key] = word

                    # Parse English synonyms and phrases
                    clean_en_raw = re.sub(r'[\(\)\[\]\{\}]', ' ', word.english.lower())
                    en_parts = [p.strip() for p in re.split(r'[,/;|\n]+', clean_en_raw) if p.strip()]
                    
                    for part in en_parts:
                        clean_part = re.sub(r'^[a-z]+\.\s*', '', part).strip() # e.g. "e.g."
                        if clean_part:
                            if clean_part not in self._english_exact_map:
                                self._english_exact_map[clean_part] = word
                            # Also index space-separated and hyphen-separated variants
                            spaced_part = re.sub(r'[-_]', ' ', clean_part).strip()
                            if spaced_part not in self._english_exact_map:
                                self._english_exact_map[spaced_part] = word
                            hyphen_part = spaced_part.replace(' ', '-')
                            if hyphen_part not in self._english_exact_map:
                                self._english_exact_map[hyphen_part] = word

                            self._english_map.setdefault(clean_part, []).append(word)
                            if spaced_part != clean_part:
                                self._english_map.setdefault(spaced_part, []).append(word)

                            # If it's a short multi-word term (e.g. "touching feet"), index sub-tokens only if non-stopword
                            for token in spaced_part.split():
                                if token not in STOPWORDS_EN and len(token) > 1:
                                    if token not in self._english_exact_map and len(en_parts) == 1 and len(spaced_part.split()) == 1:
                                        self._english_exact_map[token] = word
                                    self._english_map.setdefault(token, []).append(word)

                    # Parse Hindi synonyms and phrases
                    clean_hi_raw = re.sub(r'[\(\)\[\]\{\}]', ' ', word.hindi)
                    hi_parts = [p.strip() for p in re.split(r'[,/;|\n]+', clean_hi_raw) if p.strip()]
                    for part in hi_parts:
                        if part:
                            if part not in self._hindi_exact_map:
                                self._hindi_exact_map[part] = word
                            self._hindi_map.setdefault(part, []).append(word)
                            for token in part.split():
                                if len(token) > 1:
                                    self._hindi_map.setdefault(token, []).append(word)

        # Load phrases
        phrases_path = DATA_DIR / "phrases.json"
        if phrases_path.exists():
            with open(phrases_path, "r", encoding="utf-8") as f:
                self._phrases = json.load(f)

        # Load proverbs
        proverbs_path = DATA_DIR / "proverbs.json"
        if proverbs_path.exists():
            with open(proverbs_path, "r", encoding="utf-8") as f:
                self._proverbs = json.load(f)

        # Load riddles
        riddles_path = DATA_DIR / "riddles.json"
        if riddles_path.exists():
            with open(riddles_path, "r", encoding="utf-8") as f:
                self._riddles = json.load(f)

        # Initialize full-form morphological corpus (200,000+ words)
        from kumaoni.lexicon.morphology import FullFormCorpus, MorphAnalysis
        self._corpus = FullFormCorpus.get_instance()
        if not self._corpus._is_built and words_path.exists():
            with open(words_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                self._corpus.build_corpus(raw_data)

    def lookup(self, query: str) -> Optional[Word]:
        """
        Exact lookup for a word in Kumaoni (Devanagari), Romanized phonetic, English, or Hindi.
        Supports all base lemmas as well as 200,000+ inflected full-form variants via lemmatization.
        """
        if not query:
            return None
        q = query.strip()
        q_lower = q.lower()

        # 1. Exact Kumaoni Devanagari Base
        if q in self._kumaoni_map:
            return self._kumaoni_map[q]

        # 2. Inflected surface lookup via Morphological Lemmatizer
        lemma = self._corpus.lemmatize(q)
        if lemma != q and lemma in self._kumaoni_map:
            return self._kumaoni_map[lemma]

        # 3. Exact match in English (e.g. "water", "moon", "sun", "mother")
        if q_lower in self._english_exact_map:
            return self._english_exact_map[q_lower]

        # 4. Exact Romanized phonetic (e.g. "dajyu", "pailag", "bhuli")
        if q_lower in self._roman_map:
            return self._roman_map[q_lower]

        # 5. Direct token match in English
        if q_lower in self._english_map and self._english_map[q_lower]:
            return self._english_map[q_lower][0]

        # 6. Exact match in Hindi
        if q in self._hindi_exact_map:
            return self._hindi_exact_map[q]

        # 7. Direct token match in Hindi
        if q in self._hindi_map and self._hindi_map[q]:
            return self._hindi_map[q][0]

        return None

    def analyze(self, word: str):
        """Returns the full morphological breakdown (tense, aspect, person, case, number, gender, lemma) for any Kumaoni word."""
        return self._corpus.analyze(word)

    def lemmatize(self, word: str) -> str:
        """Returns the dictionary base lemma for any inflected Kumaoni word."""
        return self._corpus.lemmatize(word)

    def total_word_forms(self) -> int:
        """Returns the total number of recognized and generated unique full-form words (>200,000+ words)."""
        return self._corpus.total_forms()

    def search(self, query: str, limit: int = 15) -> List[Word]:
        """
        Searches words matching query substring across Kumaoni, English, and Hindi.
        """
        if not query:
            return []
        q = query.strip().lower()
        results: List[Word] = []
        seen = set()

        # First exact matches
        exact = self.lookup(query)
        if exact:
            results.append(exact)
            seen.add(exact.kumaoni)

        # Substring searches
        for w in self._words:
            if w.kumaoni in seen:
                continue
            if (q in w.kumaoni.lower() or
                q in w.roman.lower() or
                q in w.english.lower() or
                q in w.hindi.lower()):
                results.append(w)
                seen.add(w.kumaoni)
                if len(results) >= limit:
                    break

        return results

    def get_by_category(self, category: str) -> List[Word]:
        """Retrieve all words in a specific semantic category."""
        return [w for w in self._words if w.category.lower() == category.lower()]

    def all_words(self) -> List[Word]:
        return list(self._words)

    # Proverbs
    def get_proverbs(self) -> List[Dict[str, Any]]:
        return list(self._proverbs)

    def random_proverb(self) -> Dict[str, Any]:
        return random.choice(self._proverbs) if self._proverbs else {}

    # Riddles
    def get_riddles(self) -> List[Dict[str, Any]]:
        return list(self._riddles)

    def random_riddle(self) -> Dict[str, Any]:
        return random.choice(self._riddles) if self._riddles else {}

    # Phrases
    def get_phrases(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        if category:
            return [p for p in self._phrases if p.get("category", "").lower() == category.lower()]
        return list(self._phrases)

    @property
    def words(self) -> List[Word]:
        """Returns the full list of all words loaded in the lexicon."""
        return list(self._words)

    def all_words(self) -> List[Word]:
        """Returns the full list of all words loaded in the lexicon."""
        return list(self._words)

    def __len__(self) -> int:
        """Returns the total number of words in the lexicon."""
        return len(self._words)

    def random_phrase(self) -> Dict[str, Any]:
        return random.choice(self._phrases) if self._phrases else {}


# Convenience module-level instances & functions
def get_lexicon() -> Lexicon:
    return Lexicon.get_instance()


def lookup(query: str) -> Optional[Word]:
    return get_lexicon().lookup(query)


def search(query: str, limit: int = 15) -> List[Word]:
    return get_lexicon().search(query, limit=limit)


def lemmatize(word: str) -> str:
    """Returns the dictionary base lemma for any inflected Kumaoni word."""
    return get_lexicon().lemmatize(word)


def analyze(word: str):
    """Returns the full morphological breakdown for any Kumaoni word."""
    return get_lexicon().analyze(word)


def total_word_forms() -> int:
    """Returns the total number of recognized and generated unique full-form words (>200,000+ words)."""
    return get_lexicon().total_word_forms()

