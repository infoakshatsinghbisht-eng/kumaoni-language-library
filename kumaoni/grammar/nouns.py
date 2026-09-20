"""
Kumaoni noun morphology, pluralization, and grammatical cases.
"""

from typing import Dict, Optional
from kumaoni.constants import Gender, GrammaticalNumber
from kumaoni.grammar.postpositions import attach_case


def pluralize(noun: str, gender: Optional[Gender] = None) -> str:
    """
    Pluralizes a Kumaoni noun according to morphological rules.
    - Masculine ending in 'ो' (-o) changes to 'ा' (-a): घ्वड़ो -> घ्वड़ा
    - Feminine ending in 'ी' (-ee) or 'ि' (-i) adds 'यन' (-yan): चेलि -> चेलियन, डाली -> डालियन
    - Consonant endings typically remain invariant in direct nominative or take '-न': घर -> घर
    """
    if not noun:
        return ""
        
    # Ending in -o (Devanagari ो)
    if noun.endswith("ो"):
        return noun[:-1] + "ा"
        
    # Ending in -i / -ee (Devanagari ि or ी)
    if noun.endswith("ी") or noun.endswith("ि"):
        base = noun[:-1]
        return base + "ियन"
        
    return noun


def decline_noun(noun: str, case_type: str) -> str:
    """
    Declines a noun with a specific case marker.
    E.g. decline_noun('गाँव', 'ablative') -> 'गाँव बटि'
         decline_noun('ईजा', 'accusative_dative') -> 'ईजा कणी'
    """
    return attach_case(noun, case_type)


def make_diminutive(noun: str) -> str:
    """
    Converts a noun to its diminutive (smaller/affectionate) form in Kumaoni.
    - Large structure 'कूड़' -> 'कूड़ि' (cottage)
    - Basket 'डाला' / 'डालो' -> 'डाली' (small basket)
    - Buffalo 'भैंसो' -> 'भैंसी' (regular/small buffalo)
    - Path 'बाट' -> 'बाटी' (narrow trail)
    - Pot 'लोटो' -> 'लोटिया' (small pot)
    """
    if not noun:
        return ""
    if noun.endswith("ो") or noun.endswith("ा"):
        return noun[:-1] + "ी"
    if noun.endswith("ड़") or noun.endswith("ट") or noun.endswith("ल"):
        return noun + "ि"
    return noun + "ी"


def make_augmentative(noun: str) -> str:
    """
    Converts a noun to its augmentative (larger/honorific/coarse) form in Kumaoni.
    - 'कूड़ि' -> 'कूड़'
    - 'डाली' -> 'डाला'
    - 'बाटी' -> 'बाट'
    """
    if not noun:
        return ""
    if noun.endswith("ि"):
        return noun[:-1]
    if noun.endswith("ी"):
        return noun[:-1] + "ा"
    return noun


def to_feminine(noun: str) -> str:
    """
    Converts a masculine noun to its feminine counterpart where regular.
    - 'चेलो' -> 'चेली' (son -> daughter)
    - 'बाकरो' -> 'बाकरि' (he-goat -> she-goat)
    - 'घ्वड़ो' -> 'घ्वड़ी' (stallion -> mare)
    - 'बामण' -> 'बामणी' (Brahmin priest -> priestess/wife)
    """
    if not noun:
        return ""
    if noun.endswith("ो") or noun.endswith("ा"):
        return noun[:-1] + "ी"
    if noun.endswith("ण") or noun.endswith("र") or noun.endswith("ल"):
        return noun + "ी"
    return noun + "णी"


def to_masculine(noun: str) -> str:
    """
    Converts a feminine noun to its masculine counterpart where regular.
    - 'चेली' / 'चेलि' -> 'चेलो'
    - 'घ्वड़ी' -> 'घ्वड़ो'
    - 'बाकरि' -> 'बाकरो'
    """
    if not noun:
        return ""
    if noun.endswith("ी") or noun.endswith("ि"):
        return noun[:-1] + "ो"
    return noun


def to_oblique(noun: str, is_plural: bool = False) -> str:
    """
    Forms the oblique stem of a Kumaoni noun prior to attaching postpositions.
    - Masculine in -o: 'चेलो' -> oblique 'चेला' (e.g., 'चेला कणी' - to the boy)
    - Plural oblique: adds '-न' / '-ओं' (e.g., 'घरों म', 'चेलान कणी')
    """
    if not noun:
        return ""
    if is_plural:
        if noun.endswith("ा") or noun.endswith("ो"):
            return noun[:-1] + "ान"
        if noun.endswith("ी") or noun.endswith("ि"):
            return noun[:-1] + "ियन"
        return noun + "न"
        
    if noun.endswith("ो"):
        return noun[:-1] + "ा"
    return noun

