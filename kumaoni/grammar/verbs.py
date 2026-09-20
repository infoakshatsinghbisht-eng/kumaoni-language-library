"""
Kumaoni verb conjugation engine:
- Verb root extraction
- Substantive auxiliary verb ('to be' - 'छ-')
- Action verb conjugations across tenses, persons, genders, and numbers
"""

from typing import Dict, Optional, Tuple
from kumaoni.constants import Tense, Gender, GrammaticalNumber


# Common irregular verb root mappings & conjugations
IRREGULAR_PAST = {
    "जाण": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "ग्यूँ",
        (1, GrammaticalNumber.SINGULAR, Gender.FEMININE): "गैं",
        (1, GrammaticalNumber.PLURAL, Gender.MASCULINE): "गयाँ",
        (1, GrammaticalNumber.PLURAL, Gender.FEMININE): "गयाँ",
        (2, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "गये",
        (2, GrammaticalNumber.SINGULAR, Gender.FEMININE): "गै",
        (2, GrammaticalNumber.PLURAL, Gender.MASCULINE): "गया",
        (2, GrammaticalNumber.PLURAL, Gender.FEMININE): "गयीं",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "गयो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "गै",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "गया",
        (3, GrammaticalNumber.PLURAL, Gender.FEMININE): "गयीं",
    },
    "खाण": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "खायूँ",
        (1, GrammaticalNumber.SINGULAR, Gender.FEMININE): "खाईं",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "खायो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "खाई",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "खाया",
        (3, GrammaticalNumber.PLURAL, Gender.FEMININE): "खाईं",
    },
    "करन": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "कर्यूँ",
        (1, GrammaticalNumber.SINGULAR, Gender.FEMININE): "करीं",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "कर्यो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "करी",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "कर्या",
        (3, GrammaticalNumber.PLURAL, Gender.FEMININE): "करीं",
    },
    "करण": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "कर्यूँ",
        (1, GrammaticalNumber.SINGULAR, Gender.FEMININE): "करीं",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "कर्यो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "करी",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "कर्या",
        (3, GrammaticalNumber.PLURAL, Gender.FEMININE): "करीं",
    },
    "दिन": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "दियूँ",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "दियो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "दिई",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "दिया",
    },
    "दिण": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "दियूँ",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "दियो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "दिई",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "दिया",
    },
    "लिन": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "लियूँ",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "लियो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "लिई",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "लिया",
    },
    "लिण": {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "लियूँ",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "लियो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "लिई",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "लिया",
    },
}

# Substantive auxiliary verb ('छ-' / 'ach-' - to be)
AUXILIARY_TO_BE = {
    Tense.PRESENT: {
        (1, GrammaticalNumber.SINGULAR): "छूँ",
        (1, GrammaticalNumber.PLURAL): "छां",
        (2, GrammaticalNumber.SINGULAR): "छे",
        (2, GrammaticalNumber.PLURAL): "छौ",
        (3, GrammaticalNumber.SINGULAR): "छ",
        (3, GrammaticalNumber.PLURAL): "छन",
    },
    Tense.PAST: {
        (1, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "थ्यूँ",
        (1, GrammaticalNumber.SINGULAR, Gender.FEMININE): "थीं",
        (1, GrammaticalNumber.PLURAL, Gender.MASCULINE): "थां",
        (1, GrammaticalNumber.PLURAL, Gender.FEMININE): "थीं",
        (2, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "थ्ये",
        (2, GrammaticalNumber.SINGULAR, Gender.FEMININE): "थी",
        (2, GrammaticalNumber.PLURAL, Gender.MASCULINE): "था",
        (2, GrammaticalNumber.PLURAL, Gender.FEMININE): "थिन",
        (3, GrammaticalNumber.SINGULAR, Gender.MASCULINE): "थो",
        (3, GrammaticalNumber.SINGULAR, Gender.FEMININE): "थी",
        (3, GrammaticalNumber.PLURAL, Gender.MASCULINE): "था",
        (3, GrammaticalNumber.PLURAL, Gender.FEMININE): "थिन",
    },
    Tense.FUTURE: {
        (1, GrammaticalNumber.SINGULAR): "होलूँ",
        (1, GrammaticalNumber.PLURAL): "होलां",
        (2, GrammaticalNumber.SINGULAR): "होले",
        (2, GrammaticalNumber.PLURAL): "होला",
        (3, GrammaticalNumber.SINGULAR): "होलो",
        (3, GrammaticalNumber.PLURAL): "होलन",
    },
}


def extract_root(infinitive: str) -> str:
    """
    Extracts the verb root from a Kumaoni infinitive (e.g. खाण -> खा, करन -> कर, बोलण -> बोल).
    """
    infinitive = infinitive.strip()
    if infinitive.endswith("ण") or infinitive.endswith("न"):
        root = infinitive[:-1]
        # Clean up matra at end if it was just joining consonant
        return root
    return infinitive


def conjugate_to_be(
    tense: Tense = Tense.PRESENT,
    person: int = 1,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    gender: Gender = Gender.MASCULINE,
) -> str:
    """
    Conjugates the Kumaoni substantive verb 'to be' (छ- / ach-).
    E.g.:
    conjugate_to_be(Tense.PRESENT, 1, SINGULAR) -> 'छूँ' (I am)
    conjugate_to_be(Tense.PRESENT, 3, SINGULAR) -> 'छ' (He/she is)
    conjugate_to_be(Tense.PAST, 3, SINGULAR, Gender.MASCULINE) -> 'थो' (He was)
    """
    if tense == Tense.PRESENT:
        table = AUXILIARY_TO_BE[Tense.PRESENT]
        return table.get((person, number), "छ")
    elif tense == Tense.PAST:
        table = AUXILIARY_TO_BE[Tense.PAST]
        return table.get((person, number, gender), table.get((person, number, Gender.MASCULINE), "थो"))
    elif tense == Tense.FUTURE:
        table = AUXILIARY_TO_BE[Tense.FUTURE]
        return table.get((person, number), "होलो")
    return "छ"


def conjugate(
    verb: str,
    tense: Tense = Tense.PRESENT,
    person: int = 3,
    gender: Gender = Gender.MASCULINE,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    honorific: bool = False,
) -> str:
    """
    Conjugates any Kumaoni verb across tenses, persons, genders, and numbers.
    E.g.:
    conjugate('खाण', Tense.PRESENT, 1) -> 'खान्छू' (I eat)
    conjugate('जाण', Tense.PAST, 3, Gender.MASCULINE) -> 'गयो' (He went)
    conjugate('खाण', Tense.FUTURE, 1) -> 'खालूँ' (I will eat)
    """
    verb_clean = verb.strip()
    
    # Check if this is the verb 'to be' (होण / छन)
    if verb_clean in ("होण", "छन", "छ-", "to_be"):
        return conjugate_to_be(tense, person, number, gender)
        
    root = extract_root(verb_clean)
    
    # Handle honorifics (maps 2nd sing honorific to 2nd plural form)
    if honorific and person == 2:
        number = GrammaticalNumber.PLURAL
    if honorific and person == 3:
        number = GrammaticalNumber.PLURAL
        
    if tense == Tense.PRESENT:
        if person == 1:
            return f"{root}न्छां" if number == GrammaticalNumber.PLURAL else f"{root}न्छू"
        elif person == 2:
            return f"{root}न्छा" if number == GrammaticalNumber.PLURAL else f"{root}न्छे"
        else:  # person == 3
            return f"{root}न्छन" if number == GrammaticalNumber.PLURAL else f"{root}न्छ"
            
    elif tense == Tense.PAST:
        # Check irregular past table
        if verb_clean in IRREGULAR_PAST:
            irreg_entry = IRREGULAR_PAST[verb_clean].get((person, number, gender))
            if irreg_entry:
                return irreg_entry
            # Fallback for irregular table
            default_entry = IRREGULAR_PAST[verb_clean].get((person, number, Gender.MASCULINE))
            if default_entry:
                return default_entry
                
        # Regular past conjugation
        if person == 1:
            return f"{root}याँ" if number == GrammaticalNumber.PLURAL else (f"{root}ईं" if gender == Gender.FEMININE else f"{root}यूँ")
        elif person == 2:
            return f"{root}या" if number == GrammaticalNumber.PLURAL else (f"{root}ई" if gender == Gender.FEMININE else f"{root}ये")
        else:  # person == 3
            return f"{root}या" if number == GrammaticalNumber.PLURAL else (f"{root}ई" if gender == Gender.FEMININE else f"{root}यो")
            
    elif tense == Tense.FUTURE:
        # Special future for 'जाण' -> 'जुलूँ', 'जालो'
        prefix = "जु" if (verb_clean == "जाण" and person == 1) else ("जा" if verb_clean == "जाण" else root)
        if person == 1:
            return f"{prefix}लां" if number == GrammaticalNumber.PLURAL else f"{prefix}लूँ"
        elif person == 2:
            return f"{prefix}ला" if number == GrammaticalNumber.PLURAL else f"{prefix}ले"
        else:  # person == 3
            if number == GrammaticalNumber.PLURAL:
                return f"{prefix}लन"
            return f"{prefix}ली" if gender == Gender.FEMININE else f"{prefix}लो"
            
    elif tense == Tense.PRESENT_CONTINUOUS:
        aux = conjugate_to_be(Tense.PRESENT, person, number, gender)
        return f"{verb_clean} लाग्यूरूँ" if person == 1 and number == GrammaticalNumber.SINGULAR else f"{verb_clean} लाग्युं {aux}"
        
    elif tense == Tense.IMPERATIVE:
        if honorific or number == GrammaticalNumber.PLURAL:
            return f"{root}या" if root.endswith(("ा", "ो", "ू")) else f"{root}िया"
        return root
        
    return f"{root}न्छ"


def conjunctive_participle(verb: str) -> str:
    """
    Forms the Kumaoni conjunctive participle ('having done X', equivalent to Hindi '-कर').
    Uses the characteristic Kumaoni '-बेर' / '-इबेर' suffix.
    E.g.:
    conjunctive_participle('खाण') -> 'खाईबेर' (having eaten)
    conjunctive_participle('जाण') -> 'जाईबेर' (having gone)
    conjunctive_participle('देखण') -> 'देखिबेर' (having seen)
    conjunctive_participle('करण') -> 'करिबेर' (having done)
    """
    root = extract_root(verb)
    if root.endswith("ा") or root.endswith("ो") or root.endswith("ू"):
        return f"{root}ईबेर"
    return f"{root}िबेर"


def agent_noun(verb: str) -> str:
    """
    Forms the Kumaoni agentive noun ('one who does X', equivalent to Hindi '-वाला').
    Uses the authentic Kumaoni '-ण्या' suffix.
    E.g.:
    agent_noun('खाण') -> 'खाण्या' (eater)
    agent_noun('गाण') -> 'गाण्या' (singer)
    agent_noun('बोलण') -> 'बोलण्या' (speaker)
    agent_noun('लिकण') -> 'लिखण्या' (writer)
    """
    root = extract_root(verb)
    return f"{root}ण्या"


def imperative(verb: str, polite: bool = True, plural: bool = False) -> str:
    """
    Forms the Kumaoni imperative command / polite request.
    E.g.:
    imperative('खाण', polite=False) -> 'खा' (Eat!)
    imperative('खाण', polite=True) -> 'खाया' (Please eat)
    imperative('औण', polite=True) -> 'आया' (Please come)
    imperative('बैठण', polite=True) -> 'बैठिया' (Please sit)
    """
    verb_clean = verb.strip()
    if verb_clean == "औण":
        return "आया" if (polite or plural) else "आ"
    if verb_clean == "जाण":
        return "जाया" if (polite or plural) else "जा"

    root = extract_root(verb_clean)
    if not polite and not plural:
        return root
    if root.endswith("ा") or root.endswith("ो") or root.endswith("ू") or root.endswith("ौ"):
        return f"{root}या"
    return f"{root}िया"


