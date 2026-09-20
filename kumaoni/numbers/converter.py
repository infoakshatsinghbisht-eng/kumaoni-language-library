"""
Kumaoni number converter:
- Integer to Kumaoni words (0 to 10^12)
- Kumaoni words back to numbers
- Devanagari numerals conversion (०, १, २, ३, ४, ५, ६, ७, ८, ९)
- Ordinals (पैलो, दुसर, तेसर...) and fractions (आधो, सवा, डेढ़...)
"""

from typing import Dict, Union

# 0 to 100 in Kumaoni (Devanagari and phonetic Romanized)
KUMAONI_NUMS_0_TO_99: Dict[int, Dict[str, str]] = {
    0: {"dev": "शून्य", "rom": "shunya"},
    1: {"dev": "एक", "rom": "ek"},
    2: {"dev": "द्वी", "rom": "dwi"},
    3: {"dev": "तीन", "rom": "teen"},
    4: {"dev": "चार", "rom": "chaar"},
    5: {"dev": "पाँच", "rom": "paanch"},
    6: {"dev": "छ", "rom": "chhay"},
    7: {"dev": "सात", "rom": "saat"},
    8: {"dev": "आठ", "rom": "aath"},
    9: {"dev": "नौ", "rom": "nau"},
    10: {"dev": "दस", "rom": "das"},
    11: {"dev": "ग्यार", "rom": "gyaar"},
    12: {"dev": "बार", "rom": "baar"},
    13: {"dev": "तेर", "rom": "ter"},
    14: {"dev": "चौद", "rom": "chaud"},
    15: {"dev": "पंद्र", "rom": "pandr"},
    16: {"dev": "सोल", "rom": "sol"},
    17: {"dev": "सत्र", "rom": "satr"},
    18: {"dev": "अठार", "rom": "athaar"},
    19: {"dev": "उन्नीस", "rom": "unnees"},
    20: {"dev": "बीस", "rom": "bees"},
    21: {"dev": "इक्कीस", "rom": "ikkees"},
    22: {"dev": "बाईस", "rom": "baees"},
    23: {"dev": "तेईस", "rom": "te-ees"},
    24: {"dev": "चौबीस", "rom": "chaubees"},
    25: {"dev": "पच्चीस", "rom": "pachchees"},
    26: {"dev": "छब्बीस", "rom": "chhabbees"},
    27: {"dev": "सत्ताईस", "rom": "sattaees"},
    28: {"dev": "अट्ठाईस", "rom": "atthaees"},
    29: {"dev": "उनतीस", "rom": "unatees"},
    30: {"dev": "तीस", "rom": "tees"},
    31: {"dev": "इकतीस", "rom": "ikatees"},
    32: {"dev": "बत्तीस", "rom": "battees"},
    33: {"dev": "तैंतीस", "rom": "taintees"},
    34: {"dev": "चौंतीस", "rom": "chauntees"},
    35: {"dev": "पैंतीस", "rom": "paintees"},
    36: {"dev": "छत्तीस", "rom": "chhattees"},
    37: {"dev": "सैंतीस", "rom": "saintees"},
    38: {"dev": "अड़तीस", "rom": "adatees"},
    39: {"dev": "उनतालीस", "rom": "untalees"},
    40: {"dev": "चालीस", "rom": "chalees"},
    41: {"dev": "इकतालीस", "rom": "iktalees"},
    42: {"dev": "बयालीस", "rom": "bayalees"},
    43: {"dev": "तैंतालीस", "rom": "taintalees"},
    44: {"dev": "चवालीस", "rom": "chawalees"},
    45: {"dev": "पैंतालीस", "rom": "paintalees"},
    46: {"dev": "छियालीस", "rom": "chhiyalees"},
    47: {"dev": "सैंतालीस", "rom": "saintalees"},
    48: {"dev": "अड़तालीस", "rom": "adtalees"},
    49: {"dev": "उनचास", "rom": "unchaas"},
    50: {"dev": "पचास", "rom": "pachaas"},
    51: {"dev": "इक्यावन", "rom": "ikyaawan"},
    52: {"dev": "बावन", "rom": "baawan"},
    53: {"dev": "तिरेपन", "rom": "tirepan"},
    54: {"dev": "चौवन", "rom": "chauwan"},
    55: {"dev": "पचपन", "rom": "pachpan"},
    56: {"dev": "छप्पन", "rom": "chhappan"},
    57: {"dev": "सत्तावन", "rom": "sattawan"},
    58: {"dev": "अट्ठावन", "rom": "atthawan"},
    59: {"dev": "उनसठ", "rom": "unsath"},
    60: {"dev": "साठ", "rom": "saath"},
    61: {"dev": "इकसठ", "rom": "iksath"},
    62: {"dev": "बासठ", "rom": "baasath"},
    63: {"dev": "तिरसठ", "rom": "tirsath"},
    64: {"dev": "चौंसठ", "rom": "chaunsath"},
    65: {"dev": "पैंसठ", "rom": "painsath"},
    66: {"dev": "छियासठ", "rom": "chhiyasath"},
    67: {"dev": "सरसठ", "rom": "sarsath"},
    68: {"dev": "अड़सठ", "rom": "adsath"},
    69: {"dev": "उनहत्तर", "rom": "unhattar"},
    70: {"dev": "सत्तर", "rom": "sattar"},
    71: {"dev": "इकहत्तर", "rom": "ikhattar"},
    72: {"dev": "बहत्तर", "rom": "bahattar"},
    73: {"dev": "तिहत्तर", "rom": "tihattar"},
    74: {"dev": "चौहत्तर", "rom": "chauhattar"},
    75: {"dev": "पचहत्तर", "rom": "pachhattar"},
    76: {"dev": "छियाहत्तर", "rom": "chhiyaahattar"},
    77: {"dev": "सतहत्तर", "rom": "sathattar"},
    78: {"dev": "अठहत्तर", "rom": "athhattar"},
    79: {"dev": "उन्नासी", "rom": "unnaasee"},
    80: {"dev": "अस्सी", "rom": "assee"},
    81: {"dev": "इक्यासी", "rom": "ikyaasee"},
    82: {"dev": "बयासी", "rom": "bayaasee"},
    83: {"dev": "तिरासी", "rom": "tiraasee"},
    84: {"dev": "चौरासी", "rom": "chauraasee"},
    85: {"dev": "पचासी", "rom": "pachaasee"},
    86: {"dev": "छियासी", "rom": "chhiyaasee"},
    87: {"dev": "सतासी", "rom": "sataasee"},
    88: {"dev": "अठासी", "rom": "athaasee"},
    89: {"dev": "नवासी", "rom": "nawaasee"},
    90: {"dev": "नब्बे", "rom": "nabbe"},
    91: {"dev": "इक्यानवे", "rom": "ikyaanwe"},
    92: {"dev": "बानवे", "rom": "baanwe"},
    93: {"dev": "तिरानवे", "rom": "tiraanwe"},
    94: {"dev": "चौरानवे", "rom": "chauraanwe"},
    95: {"dev": "पंचानवे", "rom": "panchaanwe"},
    96: {"dev": "छियानवे", "rom": "chhiyaanwe"},
    97: {"dev": "सत्तानवे", "rom": "sattaanwe"},
    98: {"dev": "अट्ठानवे", "rom": "atthaanwe"},
    99: {"dev": "निन्यानवे", "rom": "ninyaanwe"},
}

LARGE_POWERS = [
    (10**7, {"dev": "करोड़", "rom": "karor"}),
    (10**5, {"dev": "लाख", "rom": "laakh"}),
    (10**3, {"dev": "हज़ार", "rom": "hazaar"}),
    (10**2, {"dev": "सौ", "rom": "sau"}),
]

DEV_NUMERALS = "०१२३४५६७८९"


def to_devanagari_numerals(number: Union[int, str]) -> str:
    """Converts an Arabic number (e.g. 123) to Devanagari numerals (१२३)."""
    s = str(number)
    trans = str.maketrans("0123456789", DEV_NUMERALS)
    return s.translate(trans)


def from_devanagari_numerals(text: str) -> int:
    """Converts Devanagari numerals (e.g. १२३) to an integer (123)."""
    trans = str.maketrans(DEV_NUMERALS, "0123456789")
    clean = text.translate(trans)
    return int(clean)


def num_to_words(number: int, script: str = "devanagari") -> str:
    """
    Converts an integer to Kumaoni words.
    E.g.:
    num_to_words(2) -> 'द्वी'
    num_to_words(42) -> 'बयालीस'
    num_to_words(105) -> 'एक सौ पाँच'
    """
    key = "dev" if script.lower() in ("devanagari", "dev") else "rom"
    
    if number < 0:
        neg = "माइनस " if key == "dev" else "minus "
        return neg + num_to_words(abs(number), script=script)
        
    if number in KUMAONI_NUMS_0_TO_99:
        return KUMAONI_NUMS_0_TO_99[number][key]
        
    parts = []
    curr = number
    
    for power, name_dict in LARGE_POWERS:
        unit_name = name_dict[key]
        if curr >= power:
            quotient = curr // power
            curr %= power
            parts.append(f"{num_to_words(quotient, script=script)} {unit_name}")
            
    if curr > 0:
        parts.append(KUMAONI_NUMS_0_TO_99[curr][key])
        
    return " ".join(parts)


def ordinal(number: int, script: str = "devanagari") -> str:
    """
    Returns the ordinal form of a number in Kumaoni (1st, 2nd, etc.).
    E.g. 1 -> 'पैलो' (Pailo), 2 -> 'दुसर' (Dusar), 3 -> 'तेसर' (Tesar).
    """
    is_dev = script.lower() in ("devanagari", "dev")
    ordinals_map = {
        1: ("पैलो", "pailo"),
        2: ("दुसर", "dusar"),
        3: ("तेसर", "tesar"),
        4: ("चौथो", "chautho"),
        5: ("पाँचवों", "paanchwon"),
        6: ("छठों", "chhathon"),
        7: ("सातवों", "saatwon"),
        8: ("आठवों", "aathwon"),
        9: ("नौवों", "nauwon"),
        10: ("दसवां", "daswaan"),
    }
    
    if number in ordinals_map:
        return ordinals_map[number][0 if is_dev else 1]
    
    base = num_to_words(number, script=script)
    suffix = "वों" if is_dev else "-won"
    return f"{base}{suffix}"


def fraction(numerator: int, denominator: int, script: str = "devanagari") -> str:
    """
    Returns customary Pahari / Kumaoni fraction names.
    E.g. (1, 2) -> 'आधो' (half), (1, 4) -> 'पाव' (quarter), (3, 4) -> 'पौण'.
    """
    is_dev = script.lower() in ("devanagari", "dev")
    fractions_map = {
        (1, 4): ("पाव", "paav"),
        (1, 2): ("आधो", "aadho"),
        (3, 4): ("पौण", "paun"),
        (5, 4): ("सवा", "sawa"),
        (3, 2): ("डेढ़", "dedh"),
        (5, 2): ("ढाई", "dhaai"),
    }
    
    pair = (numerator, denominator)
    if pair in fractions_map:
        return fractions_map[pair][0 if is_dev else 1]
        
    num_w = num_to_words(numerator, script=script)
    den_w = ordinal(denominator, script=script)
    return f"{num_w} बटा {den_w}" if is_dev else f"{num_w} bata {den_w}"


def words_to_num(words: str) -> int:
    """
    Parses Kumaoni number words back to integer.
    """
    words = words.strip().replace("-", " ")
    
    # Inverted lookup table
    word_map = {}
    for n, d in KUMAONI_NUMS_0_TO_99.items():
        word_map[d["dev"]] = n
        word_map[d["rom"].lower()] = n
    
    # Multipliers
    multipliers = {
        "सौ": 100, "sau": 100,
        "हज़ार": 1000, "हजार": 1000, "hazaar": 1000, "hazar": 1000,
        "लाख": 100000, "laakh": 100000, "lakh": 100000,
        "करोड़": 10000000, "karor": 10000000, "crore": 10000000,
    }
    
    tokens = words.split()
    total = 0
    current = 0
    
    for tok in tokens:
        tok_clean = tok.lower()
        if tok_clean in word_map:
            current += word_map[tok_clean]
        elif tok_clean in multipliers:
            mult = multipliers[tok_clean]
            if current == 0:
                current = 1
            if mult >= 1000:
                total += current * mult
                current = 0
            else:
                current *= mult
                
    return total + current
