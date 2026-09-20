"""
Phonetics, orthography, and script conversion utilities for Kumaoni.
Supports Devanagari normalization, Latin transliteration, and syllabification.
"""

import re
import unicodedata
from typing import List, Tuple
from kumaoni.constants import Script


# Devanagari to Latin phonetic mapping table
DEV_TO_LATIN_VOWELS = {
    'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo',
    'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au', 'अं': 'an', 'अः': 'ah',
}

DEV_MATRAS_TO_LATIN = {
    'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo',
    'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',
    'ं': 'n', 'ँ': 'n', 'ः': 'h', '्': '',
}

DEV_CONSONANTS_TO_LATIN = {
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
    'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
    'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v',
    'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
    'ड़': 'd', 'ढ़': 'dh', 'क़': 'k', 'ख़': 'kh', 'ग़': 'g', 'ज़': 'z', 'फ़': 'f',
    'क्ष': 'ksh', 'त्र': 'tr', 'ज्ञ': 'gya'
}

# Latin to Devanagari mapping sorted by key length descending for greedy matching
LATIN_TO_DEV_PAIRS = [
    # Special cultural terms
    ("dajyu", "दाज्यू"), ("daju", "दाजू"), ("pailag", "पैलाग"), ("ija", "ईजा"),
    ("bubu", "बूबू"), ("aama", "आमा"), ("bhuli", "भुली"), ("chou", "छौ"),
    ("choon", "छूँ"), ("chan", "छन"), ("cha", "छ"),
    # Triple/double consonants
    ("ksh", "क्ष"), ("gya", "ज्ञ"), ("chh", "छ"), ("kh", "ख"), ("gh", "घ"),
    ("jh", "झ"), ("th", "थ"), ("dh", "ध"), ("ph", "फ"), ("bh", "भ"),
    ("sh", "श"), ("ny", "ञ"), ("ng", "ङ"), ("tr", "त्र"),
    # Vowels
    ("aa", "आ"), ("ee", "ई"), ("oo", "ऊ"), ("ai", "ऐ"), ("au", "औ"),
    ("ri", "ऋ"),
    # Single consonants
    ("k", "क"), ("g", "ग"), ("c", "च"), ("j", "ज"), ("t", "त"),
    ("d", "द"), ("n", "न"), ("p", "प"), ("b", "ब"), ("m", "म"),
    ("y", "य"), ("r", "र"), ("l", "ल"), ("v", "व"), ("w", "व"),
    ("s", "स"), ("h", "ह"), ("z", "ज़"), ("f", "फ़"),
    # Single vowels
    ("a", "अ"), ("i", "इ"), ("u", "उ"), ("e", "ए"), ("o", "ओ"),
]

# Matra mappings for consonants followed by vowels
LATIN_VOWEL_TO_MATRA = {
    "aa": "ा", "a": "", "ee": "ी", "i": "ि", "oo": "ू",
    "u": "ु", "e": "े", "ai": "ै", "o": "ो", "au": "ौ", "an": "ं",
}


def normalize_devanagari(text: str) -> str:
    """
    Standardize Kumaoni Devanagari text:
    - Normalizes Unicode composition (NFC)
    - Standardizes chandrabindu and anusvara variations
    - Normalizes common Pahari spellings (e.g., कुमाँउनी -> कुमाऊँनी)
    """
    if not text:
        return ""
    
    # Unicode NFC normalization
    normalized = unicodedata.normalize('NFC', text)
    
    # Common orthographic normalizations in Kumaoni literature
    replacements = [
        (r'कुमाँउनी', 'कुमाऊँनी'),
        (r'कुमाउनी', 'कुमाऊँनी'),
        (r'कुमाउं', 'कुमाऊँ'),
        (r'पैलाग़', 'पैलाग'),
        (r'दज्यू', 'दाज्यू'),
        (r'[\u200B-\u200D\uFEFF]', ''),  # remove zero-width spaces/joiners if unwanted
    ]
    for pattern, repl in replacements:
        normalized = re.sub(pattern, repl, normalized)
        
    return normalized


def detect_script(text: str) -> Script:
    """
    Detect whether the input text is in Devanagari or Latin script.
    """
    dev_chars = sum(1 for ch in text if '\u0900' <= ch <= '\u097F')
    latin_chars = sum(1 for ch in text if ('a' <= ch.lower() <= 'z'))
    
    if dev_chars > latin_chars:
        return Script.DEVANAGARI
    return Script.LATIN


def devanagari_to_latin(text: str) -> str:
    """
    Transliterates Kumaoni Devanagari text into readable English/Latin phonetic script.
    """
    text = normalize_devanagari(text)
    result = []
    i = 0
    length = len(text)
    
    while i < length:
        ch = text[i]
        
        # Check independent vowels
        if ch in DEV_TO_LATIN_VOWELS:
            result.append(DEV_TO_LATIN_VOWELS[ch])
            i += 1
            continue
            
        # Check consonants
        if ch in DEV_CONSONANTS_TO_LATIN:
            consonant = DEV_CONSONANTS_TO_LATIN[ch]
            
            # Look ahead for matras or virama
            if i + 1 < length:
                next_ch = text[i + 1]
                if next_ch == '्':  # Virama / halant - no inherent vowel
                    result.append(consonant)
                    i += 2
                    continue
                elif next_ch in DEV_MATRAS_TO_LATIN:
                    matra = DEV_MATRAS_TO_LATIN[next_ch]
                    result.append(consonant + matra)
                    i += 2
                    continue
            
            # Default: inherent 'a' vowel unless followed by another vowel or end of word
            if i + 1 < length and text[i + 1] in ' \t\n.,!?;:()[]{}':
                # Schwa deletion at word boundary in northern Indo-Aryan
                result.append(consonant)
            elif i + 1 == length:
                result.append(consonant)
            else:
                result.append(consonant + 'a')
            i += 1
            continue
            
        # Matra on its own (rare)
        if ch in DEV_MATRAS_TO_LATIN:
            result.append(DEV_MATRAS_TO_LATIN[ch])
            i += 1
            continue
            
        # Non-Devanagari characters (punctuation, numbers, spaces)
        result.append(ch)
        i += 1
        
    res_str = "".join(result)
    # Clean up double 'a's or redundant letters
    res_str = re.sub(r'aaa+', 'aa', res_str)
    return res_str.strip()


def latin_to_devanagari(text: str) -> str:
    """
    Transliterates phonetic Romanized/Latin Kumaoni text into Devanagari script.
    E.g.: 'dajyu' -> 'दाज्यू', 'pailag' -> 'पैलाग', 'kas cha' -> 'कस छ'
    """
    if not text:
        return ""
        
    words = text.split(" ")
    dev_words = []
    
    # Common exact word lookup for high precision
    exact_dictionary = {
        "namaskar": "नमस्कार",
        "pailag": "पैलाग",
        "dajyu": "दाज्यू",
        "daju": "दाजू",
        "bhuli": "भुली",
        "ija": "ईजा",
        "babu": "बाबु",
        "bubu": "बूबू",
        "aama": "आमा",
        "kas": "कस",
        "cha": "छ",
        "chou": "छौ",
        "choon": "छूँ",
        "chan": "छन",
        "kahan": "कहाँ",
        "kaha": "कहाँ",
        "pani": "पाणि",
        "paani": "पाणि",
        "roti": "रोटी",
        "bhaat": "भात",
        "hoye": "होय",
        "hoi": "होइ",
        "na": "ना",
        "theek": "ठीक",
        "shubh": "शुभ",
        "bhal": "भाल",
        "kumaon": "कुमाऊँ",
        "kumaoni": "कुमाऊँनी",
        "uttarakhand": "उत्तराखण्ड",
        "main": "मैं",
        "tum": "तुम",
        "hum": "हम",
        "u": "ऊ",
        "mero": "मेरो",
        "tumar": "तुमार",
        "hamar": "हमार",
    }
    
    for word in words:
        clean_w = re.sub(r'[^a-zA-Z]', '', word).lower()
        punct_prefix = re.match(r'^[^a-zA-Z]+', word)
        punct_suffix = re.search(r'[^a-zA-Z]+$', word)
        
        pref = punct_prefix.group(0) if punct_prefix else ""
        suff = punct_suffix.group(0) if punct_suffix else ""
        
        if clean_w in exact_dictionary:
            dev_words.append(pref + exact_dictionary[clean_w] + suff)
            continue
            
        # Fallback to syllable parsing
        dev_char = _transliterate_word_to_dev(clean_w)
        dev_words.append(pref + dev_char + suff)
        
    return " ".join(dev_words)


def _transliterate_word_to_dev(word: str) -> str:
    """Internal helper to convert an English phonetic word to Devanagari."""
    if not word:
        return ""
        
    consonants = {
        "ksh": "क्ष", "gya": "ज्ञ", "chh": "छ", "kh": "ख", "gh": "घ",
        "ch": "च", "jh": "झ", "th": "थ", "dh": "ध", "ph": "फ", "bh": "भ",
        "sh": "श", "k": "क", "g": "ग", "j": "ज", "t": "त", "d": "द",
        "n": "न", "p": "प", "b": "ब", "m": "म", "y": "य", "r": "र",
        "l": "ल", "v": "व", "w": "व", "s": "स", "h": "ह", "z": "ज़", "f": "फ़"
    }
    
    vowel_matras = {
        "aa": "ा", "a": "", "ee": "ी", "i": "ि", "oo": "ू",
        "u": "ु", "e": "े", "ai": "ै", "o": "ो", "au": "ौ"
    }
    
    initial_vowels = {
        "aa": "आ", "a": "अ", "ee": "ई", "i": "इ", "oo": "ऊ",
        "u": "उ", "e": "ए", "ai": "ऐ", "o": "ओ", "au": "औ"
    }
    
    out = []
    i = 0
    w_len = len(word)
    is_start = True
    
    while i < w_len:
        matched = False
        
        # If at start of syllable or word, check initial vowel
        if is_start:
            for v_key in sorted(initial_vowels.keys(), key=len, reverse=True):
                if word[i:].startswith(v_key):
                    out.append(initial_vowels[v_key])
                    i += len(v_key)
                    is_start = False
                    matched = True
                    break
            if matched:
                continue
                
        # Check consonant
        for c_key in sorted(consonants.keys(), key=len, reverse=True):
            if word[i:].startswith(c_key):
                con = consonants[c_key]
                i += len(c_key)
                
                # Check following vowel for matra
                v_matched = False
                for v_key in sorted(vowel_matras.keys(), key=len, reverse=True):
                    if word[i:].startswith(v_key):
                        out.append(con + vowel_matras[v_key])
                        i += len(v_key)
                        v_matched = True
                        break
                        
                if not v_matched:
                    # Trailing consonant or consonant cluster
                    if i < w_len and any(word[i:].startswith(k) for k in consonants):
                        out.append(con + "्")
                    else:
                        out.append(con)
                        
                is_start = False
                matched = True
                break
                
        if not matched:
            out.append(word[i])
            i += 1
            is_start = False
            
    return "".join(out)


def tokenize(text: str) -> List[str]:
    """
    Tokenizes Kumaoni text into individual words, preserving punctuation.
    """
    if not text:
        return []
    return re.findall(r'[\u0900-\u097F\w]+|[^\s\w]', text)


def syllables(word: str) -> List[str]:
    """
    Splits a Kumaoni word into phonological syllables.
    """
    norm = normalize_devanagari(word)
    # Match consonant + optional virama/matra clusters
    pattern = r'[\u0904-\u0914]|\u0915-\u0939[\u094d]?[\u093e-\u094c\u0901-\u0903]?'
    parts = re.findall(pattern, norm)
    return parts if parts else [word]
