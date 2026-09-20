"""
Kumaoni (कुमाऊँनी) Language Library for Python
=============================================

A standard-library-style Python package for the Kumaoni language, providing
linguistic primitives, phonetics, grammar, verb conjugation, dictionary lookups,
and universal translation from any language of the world into Kumaoni.

Quick Start:
------------
>>> import kumaoni
>>> kumaoni.translate("How are you?")
<TranslationResult text='कस छू तुम?' romanized='kas chhoo tum?'>
>>> kumaoni.conjugate("जाण", tense="past", person=1)
'ग्यूँ'
>>> kumaoni.num_to_words(42)
'बयालीस'
>>> kumaoni.lookup("ईजा")
Word(kumaoni='ईजा', roman='ija', english='mother', hindi='माँ', pos='noun', category='kinship')
"""

__version__ = "1.0.0"
__author__ = "Kumaoni Language Initiative"

# Constants
from kumaoni.constants import (
    ISO_639_3,
    ISO_639_NAME,
    NATIVE_NAME,
    Dialect,
    Script,
    PartOfSpeech,
    Tense,
    Gender,
    GrammaticalNumber,
    SEASONS,
    KUMAONI_MONTHS,
    DAYS_OF_WEEK,
    KINSHIP,
)

# Phonetics & Script Conversion
from kumaoni.phonetics import (
    normalize_devanagari as normalize,
    detect_script,
    devanagari_to_latin,
    latin_to_devanagari,
    tokenize,
    syllables,
)

# Numbers & Numerals
from kumaoni.numbers import (
    num_to_words,
    words_to_num,
    to_devanagari_numerals,
    from_devanagari_numerals,
    ordinal,
    fraction,
)

# Grammar & Morphology
from kumaoni.grammar import (
    extract_root,
    conjugate,
    conjugate_to_be,
    conjunctive_participle,
    agent_noun,
    imperative,
    pluralize,
    decline_noun,
    make_diminutive,
    make_augmentative,
    to_feminine,
    to_masculine,
    to_oblique,
    attach_case,
    get_marker,
    get_pronoun,
    CASE_MARKERS,
    PRONOUN_TABLE,
    SyntaxEngine,
    causative,
    passive,
    medio_passive_inability,
    compound_verb,
    echo_word,
    build_sentence,
    conditional,
    relative_correlative,
    prohibitive,
    modal_ability,
    modal_obligation,
    modal_desiderative,
    interrogative_sentence,
)

# Lexicon & Dictionary & 100k+ Morphological Engine
from kumaoni.lexicon import (
    Word,
    Lexicon,
    get_lexicon,
    lookup,
    search,
    lemmatize,
    analyze,
    total_word_forms,
    MorphAnalysis,
    KumaoniMorphology,
    FullFormCorpus,
)

# Translation Engine
from kumaoni.translator import (
    Translator,
    TranslationResult,
    translate,
    RuleBasedTranslator,
    PivotTranslator,
    LLMTranslator,
)

# Culture & Heritage
from kumaoni.culture import (
    Festival,
    get_festival,
    list_festivals,
    get_months,
    get_seasons,
    get_days_of_week,
    get_current_season,
)


# Voice & Speech Synthesis
from kumaoni.voice import (
    KumaoniVoiceSynthesizer,
    VoiceTranslator,
    VoiceTranslationResult,
    voice_translate,
)


def transliterate(text: str, to_script: str = "devanagari") -> str:
    """
    Universal transliterator between Latin and Devanagari scripts for Kumaoni.
    """
    to_s = to_script.lower()
    if to_s in ("devanagari", "dev"):
        return latin_to_devanagari(text)
    elif to_s in ("latin", "roman", "eng"):
        return devanagari_to_latin(text)
    return text


# Cultural convenience facades
class _ProverbsFacade:
    def list(self):
        return get_lexicon().get_proverbs()

    def all(self):
        return self.list()

    def random(self):
        return get_lexicon().random_proverb()


class _RiddlesFacade:
    def list(self):
        return get_lexicon().get_riddles()

    def all(self):
        return self.list()

    def random(self):
        return get_lexicon().random_riddle()


class _PhrasesFacade:
    def list(self, category=None):
        return get_lexicon().get_phrases(category=category)

    def all(self, category=None):
        return self.list(category=category)

    def random(self):
        return get_lexicon().random_phrase()


class _FestivalsFacade:
    def list(self):
        return list_festivals()

    def all(self):
        return self.list()

    def get(self, name):
        return get_festival(name)


class _LiteratureFacade:
    def epics(self):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.list_epics()

    def get_epic(self, epic_id):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.get_epic(epic_id)

    def poems(self, form=None):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.list_poems(form=form)

    def authors(self):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.list_authors()

    def get_author(self, author_id):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.get_author(author_id)


class _VoiceFacade:
    def translate(self, text: str, source_lang: str = "auto", method: str = "auto", generate_audio: bool = False):
        return voice_translate(text, source_lang=source_lang, method=method, generate_audio=generate_audio)

    def synthesize_wav(self, duration_seconds: float = 1.0, freq: float = 440.0):
        return KumaoniVoiceSynthesizer.generate_pcm_wav(duration_seconds=duration_seconds, freq=freq)

    def phrases(self, category=None):
        from kumaoni.voice.engine import _voice_translator
        return _voice_translator.get_voice_phrases(category=category)


proverbs = _ProverbsFacade()
riddles = _RiddlesFacade()
phrases = _PhrasesFacade()
festivals = _FestivalsFacade()
literature = _LiteratureFacade()
voice = _VoiceFacade()

__all__ = [
    # Top-level functions
    "translate",
    "voice_translate",
    "lookup",
    "search",
    "lemmatize",
    "analyze",
    "total_word_forms",
    "MorphAnalysis",
    "KumaoniMorphology",
    "FullFormCorpus",
    "conjugate",
    "conjugate_to_be",
    "conjunctive_participle",
    "agent_noun",
    "imperative",
    "causative",
    "passive",
    "medio_passive_inability",
    "compound_verb",
    "echo_word",
    "build_sentence",
    "conditional",
    "relative_correlative",
    "prohibitive",
    "modal_ability",
    "modal_obligation",
    "modal_desiderative",
    "interrogative_sentence",
    "num_to_words",
    "words_to_num",
    "to_devanagari_numerals",
    "from_devanagari_numerals",
    "ordinal",
    "fraction",
    "normalize",
    "transliterate",
    "devanagari_to_latin",
    "latin_to_devanagari",
    "tokenize",
    "syllables",
    "pluralize",
    "decline_noun",
    "make_diminutive",
    "make_augmentative",
    "to_feminine",
    "to_masculine",
    "to_oblique",
    "attach_case",
    "get_marker",
    "get_pronoun",
    # Voice classes
    "KumaoniVoiceSynthesizer",
    "VoiceTranslator",
    "VoiceTranslationResult",
    # Constants
    "ISO_639_3",
    "ISO_639_NAME",
    "NATIVE_NAME",
    "Dialect",
    "Script",
    "PartOfSpeech",
    "Tense",
    "Gender",
    "GrammaticalNumber",
    "SEASONS",
    "KUMAONI_MONTHS",
    "DAYS_OF_WEEK",
    "KINSHIP",
    "CASE_MARKERS",
    "PRONOUN_TABLE",
    # Facades
    "proverbs",
    "riddles",
    "phrases",
    "festivals",
    "literature",
    "voice",
]



