"""
Lexicon module for the Kumaoni language.
"""

from kumaoni.lexicon.dictionary import (
    Word,
    Lexicon,
    get_lexicon,
    lookup,
    search,
    lemmatize,
    analyze,
    total_word_forms,
)
from kumaoni.lexicon.morphology import (
    MorphAnalysis,
    KumaoniMorphology,
    FullFormCorpus,
)

__all__ = [
    "Word",
    "Lexicon",
    "get_lexicon",
    "lookup",
    "search",
    "lemmatize",
    "analyze",
    "total_word_forms",
    "MorphAnalysis",
    "KumaoniMorphology",
    "FullFormCorpus",
]

