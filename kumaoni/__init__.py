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

__version__ = "1.1.0"
__author__ = "Akshat Singh Bisht"
__email__ = "infoakshatsinghbisht@gmail.com"
__maintainer__ = "Akshat Singh Bisht"
__website__ = "https://akshatsinghbisht.com/"
__copyright__ = "Copyright (c) 2026 Akshat Singh Bisht"
__license__ = "MIT"

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
    search_festivals,
    get_months,
    get_seasons,
    get_days_of_week,
    get_current_season,
    KumaoniBook,
    BibliographyTreasury,
    KumaoniSong,
    KumaoniHoliSong,
    DigitalArchiveSource,
    FolkloreTreasury,
    KumaoniDeity,
    DeitiesTreasury,
    KumaoniPlace,
    PlacesTreasury,
    KumaoniSurname,
    SurnamesTreasury,
    KumaoniPlant,
    FloraTreasury,
    KumaoniRitualItem,
    RitualsTreasury,
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

    def search(self, query):
        return search_festivals(query)


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

    def list(self):
        return self.authors()

    def get(self, author_id):
        return self.get_author(author_id)

    def get_author(self, author_id):
        from kumaoni.culture.literature import LiteratureTreasury
        return LiteratureTreasury.get_author(author_id)

    def books(self, category=None, author=None, genre=None, query=None):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.list_books(category=category, author=author, genre=genre, query=query)

    def get_book(self, book_id):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.get_book(book_id)

    def bibliography(self, category=None, author=None, genre=None, query=None):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.list_books(category=category, author=author, genre=genre, query=query)

    def songs(self, genre=None, artist=None, corpus=None, query=None):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.list_songs(genre=genre, artist=artist, corpus=corpus, query=query)

    def get_song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_song(song_id)

    def holi_songs(self, form=None, raag=None, query=None):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.list_holi_songs(form=form, raag=raag, query=query)

    def get_holi_song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_holi_song(song_id)


class _BibliographyFacade:
    def list(self, category=None, author=None, genre=None, query=None):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.list_books(category=category, author=author, genre=genre, query=query)

    def get(self, book_id):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.get_book(book_id)

    def search(self, query):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.search(query)

    def categories(self):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.categories()

    def stats(self):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.stats()

    def authors(self):
        from kumaoni.culture.bibliography import BibliographyTreasury
        return BibliographyTreasury.authors()


class _FolkloreFacade:
    def songs(self, genre=None, artist=None, corpus=None, query=None):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.list_songs(genre=genre, artist=artist, corpus=corpus, query=query)

    def song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_song(song_id)

    def get_song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_song(song_id)

    def random_song(self):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.random_song()

    def holi_songs(self, form=None, raag=None, query=None):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.list_holi_songs(form=form, raag=raag, query=query)

    def holi_song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_holi_song(song_id)

    def get_holi_song(self, song_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_holi_song(song_id)

    def random_holi_song(self):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.random_holi_song()

    def sources(self):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.list_sources()

    def get_source(self, source_id):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.get_source(source_id)

    def stats(self):
        from kumaoni.culture.folklore import FolkloreTreasury
        return FolkloreTreasury.stats()


class _DeitiesFacade:
    def list(self, category=None):
        from kumaoni.culture.deities import DeitiesTreasury
        return DeitiesTreasury.list(category=category)

    def all(self, category=None):
        return self.list(category=category)

    def get(self, name_or_id):
        from kumaoni.culture.deities import DeitiesTreasury
        return DeitiesTreasury.get(name_or_id)

    def search(self, query):
        from kumaoni.culture.deities import DeitiesTreasury
        return DeitiesTreasury.search(query)

    def stats(self):
        from kumaoni.culture.deities import DeitiesTreasury
        return DeitiesTreasury.stats()


class _PlacesFacade:
    def list(self, category=None, district=None):
        from kumaoni.culture.places import PlacesTreasury
        return PlacesTreasury.list(category=category, district=district)

    def all(self, category=None, district=None):
        return self.list(category=category, district=district)

    def get(self, place_id):
        from kumaoni.culture.places import PlacesTreasury
        return PlacesTreasury.get(place_id)

    def search(self, query):
        from kumaoni.culture.places import PlacesTreasury
        return PlacesTreasury.search(query)

    def stats(self):
        from kumaoni.culture.places import PlacesTreasury
        return PlacesTreasury.stats()


class _SurnamesFacade:
    def list(self, community=None):
        from kumaoni.culture.surnames import SurnamesTreasury
        return SurnamesTreasury.list(community=community)

    def all(self, community=None):
        return self.list(community=community)

    def get(self, surname_id):
        from kumaoni.culture.surnames import SurnamesTreasury
        return SurnamesTreasury.get(surname_id)

    def search(self, query):
        from kumaoni.culture.surnames import SurnamesTreasury
        return SurnamesTreasury.search(query)

    def social_concepts(self):
        from kumaoni.culture.surnames import SurnamesTreasury
        return SurnamesTreasury.social_concepts()

    def stats(self):
        from kumaoni.culture.surnames import SurnamesTreasury
        return SurnamesTreasury.stats()


class _FloraFacade:
    def list(self, category=None):
        from kumaoni.culture.flora import FloraTreasury
        return FloraTreasury.list(category=category)

    def all(self, category=None):
        return self.list(category=category)

    def get(self, plant_id):
        from kumaoni.culture.flora import FloraTreasury
        return FloraTreasury.get(plant_id)

    def search(self, query):
        from kumaoni.culture.flora import FloraTreasury
        return FloraTreasury.search(query)

    def stats(self):
        from kumaoni.culture.flora import FloraTreasury
        return FloraTreasury.stats()


class _RitualsFacade:
    def list(self, category=None):
        from kumaoni.culture.rituals import RitualsTreasury
        return RitualsTreasury.list(category=category)

    def all(self, category=None):
        return self.list(category=category)

    def get(self, item_id):
        from kumaoni.culture.rituals import RitualsTreasury
        return RitualsTreasury.get(item_id)

    def search(self, query):
        from kumaoni.culture.rituals import RitualsTreasury
        return RitualsTreasury.search(query)

    def stats(self):
        from kumaoni.culture.rituals import RitualsTreasury
        return RitualsTreasury.stats()


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
bibliography = _BibliographyFacade()
folklore = _FolkloreFacade()
deities = _DeitiesFacade()
places = _PlacesFacade()
surnames = _SurnamesFacade()
flora = _FloraFacade()
rituals = _RitualsFacade()
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
    "bibliography",
    "folklore",
    "deities",
    "places",
    "surnames",
    "flora",
    "rituals",
    "voice",
    # Bibliography, Folklore, Deities, Places, Surnames, Flora & Rituals
    "KumaoniBook",
    "BibliographyTreasury",
    "KumaoniSong",
    "KumaoniHoliSong",
    "DigitalArchiveSource",
    "FolkloreTreasury",
    "KumaoniDeity",
    "DeitiesTreasury",
    "KumaoniPlace",
    "PlacesTreasury",
    "KumaoniSurname",
    "SurnamesTreasury",
    "KumaoniPlant",
    "FloraTreasury",
    "KumaoniRitualItem",
    "RitualsTreasury",
    "search_festivals",
]



