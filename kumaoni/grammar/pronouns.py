"""
Kumaoni pronoun declensions across person, number, case, and honorifics.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from kumaoni.constants import Gender, GrammaticalNumber


@dataclass
class PronounDeclension:
    person: int                      # 1, 2, 3
    number: GrammaticalNumber
    nominative: str                  # Subject (e.g. मैं, तू, तुम, ऊ)
    ergative: str                    # Agentive with -ले (e.g. मैंले, तुमले)
    accusative_dative: str           # Object with -कणी (e.g. मैंकणी, तुमकणी)
    possessive_masc: str             # मेरो, तेरो, तुमारो, उको
    possessive_fem: str              # मेरी, तेरी, तुमारी, उकी
    possessive_plural: str           # मेरा, तेरा, तुमारा, उनका
    ablative: str                    # Source with -बटि (e.g. मैंबटि)
    locative: str                    # Location with -म (e.g. मैंम)
    english: str
    hindi: str
    honorific: bool = False


PRONOUN_TABLE: List[PronounDeclension] = [
    # 1st Person Singular (I)
    PronounDeclension(
        person=1,
        number=GrammaticalNumber.SINGULAR,
        nominative="मैं",
        ergative="मैंले",
        accusative_dative="मैंकणी",
        possessive_masc="मेरो",
        possessive_fem="मेरी",
        possessive_plural="मेरा",
        ablative="मैंबटि",
        locative="मैंम",
        english="I",
        hindi="मैं",
        honorific=False
    ),
    # 1st Person Plural (We)
    PronounDeclension(
        person=1,
        number=GrammaticalNumber.PLURAL,
        nominative="हम",
        ergative="हम्ले",
        accusative_dative="हमकणी",
        possessive_masc="हमारो",
        possessive_fem="हमारी",
        possessive_plural="हमारा",
        ablative="हमबटि",
        locative="हमम",
        english="we",
        hindi="हम",
        honorific=False
    ),
    # 2nd Person Singular (You - intimate/informal)
    PronounDeclension(
        person=2,
        number=GrammaticalNumber.SINGULAR,
        nominative="तू",
        ergative="तैंले",
        accusative_dative="तुकणी",
        possessive_masc="तेरो",
        possessive_fem="तेरी",
        possessive_plural="तेरा",
        ablative="तूबटि",
        locative="तूम",
        english="you (informal)",
        hindi="तू",
        honorific=False
    ),
    # 2nd Person Plural / Respectful (You - formal/respectful)
    PronounDeclension(
        person=2,
        number=GrammaticalNumber.PLURAL,
        nominative="तुम",
        ergative="तुमले",
        accusative_dative="तुमकणी",
        possessive_masc="तुमारो",
        possessive_fem="तुमारी",
        possessive_plural="तुमारा",
        ablative="तुमबटि",
        locative="तुमम",
        english="you (formal / plural)",
        hindi="आप / तुम",
        honorific=True
    ),
    # 3rd Person Singular Proximate (This / He / She nearby)
    PronounDeclension(
        person=3,
        number=GrammaticalNumber.SINGULAR,
        nominative="यो",
        ergative="यिले",
        accusative_dative="यिकणी",
        possessive_masc="यिको",
        possessive_fem="यिकी",
        possessive_plural="यिका",
        ablative="यिबटि",
        locative="यिम",
        english="this / he / she (proximate)",
        hindi="यह",
        honorific=False
    ),
    # 3rd Person Singular Distal (That / He / She far)
    PronounDeclension(
        person=3,
        number=GrammaticalNumber.SINGULAR,
        nominative="ऊ",
        ergative="उले",
        accusative_dative="उकणी",
        possessive_masc="उको",
        possessive_fem="उकी",
        possessive_plural="उका",
        ablative="उबटि",
        locative="उम",
        english="that / he / she (distal)",
        hindi="वह",
        honorific=False
    ),
    # 3rd Person Plural (They / Those)
    PronounDeclension(
        person=3,
        number=GrammaticalNumber.PLURAL,
        nominative="ऊँ",
        ergative="उनले",
        accusative_dative="उनकणी",
        possessive_masc="उनको",
        possessive_fem="उनकी",
        possessive_plural="उनका",
        ablative="उनबटि",
        locative="उनम",
        english="they",
        hindi="वे / वो",
        honorific=False
    ),
]


def get_pronoun(
    person: int,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    honorific: bool = False
) -> Optional[PronounDeclension]:
    """Retrieve pronoun declension matching person, number, and honorific flag."""
    for p in PRONOUN_TABLE:
        if p.person == person and p.number == number:
            if honorific and not p.honorific and person == 2:
                continue
            return p
    return None
