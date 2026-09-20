"""
Linguistic and cultural constants for the Kumaoni language library.
"""

from enum import Enum


class Dialect(str, Enum):
    """Major regional dialects of the Kumaoni language."""
    STANDARD = "standard"          # Central / Almora / Majh-Kumaiya standard
    KHASPARJIYA = "khasparjiya"    # Almora and surrounding hilly heartland
    SORYALI = "soryali"            # Pithoragarh / Soar valley
    GANGOLI = "gangoli"            # Gangolihat region
    ASKOTI = "askoti"              # Askot / Didihat region
    DANPURIYA = "danpuriya"        # Danpur / Bageshwar region
    SIRWALI = "sirwali"            # Siragadh region
    CHAUGAARKHIYA = "chaugaarkhiya" # Champawat / Kali Kumaon
    JOHARI = "johari"              # Johar valley / Munsiyari (northern borderland)


class Script(str, Enum):
    """Scripts supported for Kumaoni."""
    DEVANAGARI = "devanagari"
    LATIN = "latin"                # Romanized / English phonetic
    IAST = "iast"                  # International Alphabet of Sanskrit Transliteration


class PartOfSpeech(str, Enum):
    """Linguistic parts of speech."""
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    POSTPOSITION = "postposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    PARTICLE = "particle"
    NUMBER = "number"


class Tense(str, Enum):
    """Grammatical tenses."""
    PRESENT = "present"
    PAST = "past"
    FUTURE = "future"
    PRESENT_CONTINUOUS = "present_continuous"
    PAST_CONTINUOUS = "past_continuous"
    FUTURE_CONTINUOUS = "future_continuous"
    IMPERATIVE = "imperative"


class Gender(str, Enum):
    """Grammatical genders."""
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTER = "neuter"


class GrammaticalNumber(str, Enum):
    """Grammatical numbers."""
    SINGULAR = "singular"
    PLURAL = "plural"


# ISO language code for Kumaoni
ISO_639_3 = "kfy"
ISO_639_NAME = "Kumaoni"
NATIVE_NAME = "कुमाऊँनी"

# Traditional Kumaoni Seasons (ऋतु / Ritu)
SEASONS = {
    "basant": {"name_kmy": "बसंत", "english": "Spring", "months": ["फागुन", "चैत"]},
    "grishma": {"name_kmy": "रूड़ि", "english": "Summer", "months": ["बैसाख", "जेठ"]},
    "varsha": {"name_kmy": "चौमास", "english": "Monsoon / Rainy", "months": ["असाड़", "साउन", "भादौ"]},
    "sharad": {"name_kmy": "सरद", "english": "Autumn", "months": ["आसोज", "कातिक"]},
    "hemant": {"name_kmy": "स्यूँद", "english": "Early Winter", "months": ["मंगसिर", "पूस"]},
    "shishir": {"name_kmy": "जाड़", "english": "Late Winter", "months": ["माघ", "फागुन"]},
}

# Kumaoni Solar Calendar Months (सौर मास)
KUMAONI_MONTHS = [
    {"index": 1, "kumaoni": "चैत", "roman": "Chait", "gregorian": "March-April"},
    {"index": 2, "kumaoni": "बैसाख", "roman": "Baisakh", "gregorian": "April-May"},
    {"index": 3, "kumaoni": "जेठ", "roman": "Jeth", "gregorian": "May-June"},
    {"index": 4, "kumaoni": "असाड़", "roman": "Asadh", "gregorian": "June-July"},
    {"index": 5, "kumaoni": "साउन", "roman": "Saun", "gregorian": "July-August"},
    {"index": 6, "kumaoni": "भादौ", "roman": "Bhado", "gregorian": "August-September"},
    {"index": 7, "kumaoni": "आसोज", "roman": "Aasoj", "gregorian": "September-October"},
    {"index": 8, "kumaoni": "कातिक", "roman": "Kaatik", "gregorian": "October-November"},
    {"index": 9, "kumaoni": "मंगसिर", "roman": "Mangasir", "gregorian": "November-December"},
    {"index": 10, "kumaoni": "पूस", "roman": "Poos", "gregorian": "December-January"},
    {"index": 11, "kumaoni": "माघ", "roman": "Maagh", "gregorian": "January-February"},
    {"index": 12, "kumaoni": "फागुन", "roman": "Faagun", "gregorian": "February-March"},
]

# Days of the Week
DAYS_OF_WEEK = [
    {"day": 0, "kumaoni": "इतवार", "roman": "Itwaar", "english": "Sunday"},
    {"day": 1, "kumaoni": "सोमवार", "roman": "Somwaar", "english": "Monday"},
    {"day": 2, "kumaoni": "मंगलवार", "roman": "Mangalwaar", "english": "Tuesday"},
    {"day": 3, "kumaoni": "बुधवार", "roman": "Budhwaar", "english": "Wednesday"},
    {"day": 4, "kumaoni": "बिसवार", "roman": "Biswaar", "english": "Thursday"},
    {"day": 5, "kumaoni": "सुकरवार", "roman": "Sukarwaar", "english": "Friday"},
    {"day": 6, "kumaoni": "सनिच्चर", "roman": "Sanicchar", "english": "Saturday"},
]

# Common Kinship Terms
KINSHIP = {
    "father": {"kumaoni": "बाबु", "variants": ["बौजी", "बुबा"], "roman": "Babu / Bauji"},
    "mother": {"kumaoni": "ईजा", "variants": ["म्यात"], "roman": "Ija"},
    "elder_brother": {"kumaoni": "दाज्यू", "variants": ["दाजू"], "roman": "Dajyu"},
    "younger_brother": {"kumaoni": "भै", "variants": ["भैया"], "roman": "Bhai"},
    "elder_sister": {"kumaoni": "दीदी", "variants": ["दिदी"], "roman": "Didi"},
    "younger_sister": {"kumaoni": "भुली", "variants": ["बैणी"], "roman": "Bhuli / Baini"},
    "grandfather": {"kumaoni": "बूबू", "variants": ["बारबाबू"], "roman": "Bubu"},
    "grandmother": {"kumaoni": "आमा", "variants": ["अम्मा"], "roman": "Aama"},
    "son": {"kumaoni": "च्याल", "variants": ["च्यल"], "roman": "Chyal"},
    "daughter": {"kumaoni": "चेलि", "variants": ["चेली"], "roman": "Cheli"},
    "uncle_paternal": {"kumaoni": "काका", "variants": ["काकू"], "roman": "Kaka"},
    "aunt_paternal": {"kumaoni": "काकी", "variants": [], "roman": "Kaki"},
    "children": {"kumaoni": "नान्तिन", "variants": ["नतुवे"], "roman": "Naantin"},
}
