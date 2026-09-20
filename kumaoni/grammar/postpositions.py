"""
Kumaoni case markers (कारक / Karaka) and postpositions.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class CaseMarker:
    case_name: str
    hindi_equivalent: str
    english_equivalent: str
    kumaoni_forms: List[str]
    description: str


CASE_MARKERS: Dict[str, CaseMarker] = {
    "nominative_agentive": CaseMarker(
        case_name="कर्ता (Ergative/Agentive)",
        hindi_equivalent="ने",
        english_equivalent="by / (subject marker)",
        kumaoni_forms=["ले", "ल"],
        description="Used with transitive subjects in perfective/past tenses (e.g., 'रामले खायो' - Ram ate)."
    ),
    "accusative_dative": CaseMarker(
        case_name="कर्म / संप्रदान (Objective/Dative)",
        hindi_equivalent="को / के लिए",
        english_equivalent="to / for",
        kumaoni_forms=["कणी", "कण", "कै", "हुणि", "हूँ"],
        description="Direct and indirect object marker (e.g., 'मैंकणी दी' - Give to me)."
    ),
    "instrumental": CaseMarker(
        case_name="करण (Instrumental)",
        hindi_equivalent="से / के द्वारा",
        english_equivalent="with / by means of",
        kumaoni_forms=["ले", "जरियाल", "हातै"],
        description="Instrument or means (e.g., 'कलमले लिक' - Write with pen)."
    ),
    "ablative": CaseMarker(
        case_name="अपादान (Ablative)",
        hindi_equivalent="से (अलग होना / तुलना)",
        english_equivalent="from / than",
        kumaoni_forms=["बटि", "हैं", "थैं", "बट"],
        description="Source, separation or comparison (e.g., 'घरबटि' - from home, 'उहैं भाल' - better than him)."
    ),
    "genitive": CaseMarker(
        case_name="संबंध (Genitive/Possessive)",
        hindi_equivalent="का / की / के",
        english_equivalent="of / 's",
        kumaoni_forms=["को", "की", "का", "क"],
        description="Possession (e.g., 'पहाड़क पाणि' - Water of hills, 'रामको घर' - Ram's house)."
    ),
    "locative": CaseMarker(
        case_name="अधिकरण (Locative)",
        hindi_equivalent="में / पर",
        english_equivalent="in / on / at",
        kumaoni_forms=["म", "में", "पं", "पर", "भितर"],
        description="Spatial or temporal location (e.g., 'गाँवक भितर' - inside village, 'रूख पं' - on tree)."
    ),
    "sociative_comitative": CaseMarker(
        case_name="सहयोग / सहकार (Comitative/Sociative)",
        hindi_equivalent="के साथ / के संग",
        english_equivalent="with / along with",
        kumaoni_forms=["दगड़", "दगड़े", "संग", "साथ"],
        description="Accompaniment or partnership (e.g., 'इजा दगड़' - with mother, 'भै दगड़े' - alongside brother)."
    ),
    "terminative": CaseMarker(
        case_name="सीमा बोधक (Terminative/Limitative)",
        hindi_equivalent="तक / पर्यन्त",
        english_equivalent="up to / until / as far as",
        kumaoni_forms=["तक", "तलक", "सम्म", "कणि"],
        description="Limit of time or space (e.g., 'सांझ तक' - until evening, 'शिखर तलक' - up to the summit)."
    ),
    "locative_superior": CaseMarker(
        case_name="ऊर्ध्व स्थान (Superior Locative)",
        hindi_equivalent="के ऊपर / चोटी पर",
        english_equivalent="above / on top of / upon",
        kumaoni_forms=["मायि", "मथि", "मलि"],
        description="Position higher up on hill or tree (e.g., 'डाँड़ा मायि' - on top of ridge)."
    ),
    "locative_inferior": CaseMarker(
        case_name="अधो स्थान (Inferior Locative)",
        hindi_equivalent="के नीचे / तलहटी में",
        english_equivalent="under / below / underneath",
        kumaoni_forms=["मुणि", "तलि", "निसि"],
        description="Position down below or in the valley (e.g., 'बोट मुणि' - under the tree)."
    ),
}


def get_marker(case_type: str) -> Optional[CaseMarker]:
    """Retrieve details for a specific Kumaoni grammatical case marker."""
    return CASE_MARKERS.get(case_type.lower())


def attach_case(noun: str, case_type: str, form_index: int = 0) -> str:
    """
    Attaches a Kumaoni case marker postposition to a noun.
    E.g.: attach_case('राम', 'nominative_agentive') -> 'रामले'
          attach_case('घर', 'ablative') -> 'घरबटि'
    """
    marker = CASE_MARKERS.get(case_type.lower())
    if not marker:
        raise ValueError(f"Unknown case type '{case_type}'. Available: {list(CASE_MARKERS.keys())}")
        
    form = marker.kumaoni_forms[min(form_index, len(marker.kumaoni_forms) - 1)]
    return f"{noun}{form}" if form in ("ले", "ल") else f"{noun} {form}"
