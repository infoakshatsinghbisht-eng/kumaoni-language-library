"""
Grammar module for the Kumaoni language.
"""

from kumaoni.grammar.postpositions import CaseMarker, CASE_MARKERS, get_marker, attach_case
from kumaoni.grammar.pronouns import PronounDeclension, PRONOUN_TABLE, get_pronoun
from kumaoni.grammar.nouns import (
    pluralize,
    decline_noun,
    make_diminutive,
    make_augmentative,
    to_feminine,
    to_masculine,
    to_oblique,
)
from kumaoni.grammar.verbs import (
    extract_root,
    conjugate,
    conjugate_to_be,
    conjunctive_participle,
    agent_noun,
    imperative,
)

from kumaoni.grammar.syntax import (
    SyntaxEngine,
)

causative = SyntaxEngine.causative
passive = SyntaxEngine.passive
medio_passive_inability = SyntaxEngine.medio_passive_inability
compound_verb = SyntaxEngine.compound_verb
echo_word = SyntaxEngine.echo_word
build_sentence = SyntaxEngine.build_sentence
conditional = SyntaxEngine.conditional
relative_correlative = SyntaxEngine.relative_correlative
prohibitive = SyntaxEngine.prohibitive
modal_ability = SyntaxEngine.modal_ability
modal_obligation = SyntaxEngine.modal_obligation
modal_desiderative = SyntaxEngine.modal_desiderative
interrogative_sentence = SyntaxEngine.interrogative_sentence

__all__ = [
    "CaseMarker",
    "CASE_MARKERS",
    "get_marker",
    "attach_case",
    "PronounDeclension",
    "PRONOUN_TABLE",
    "get_pronoun",
    "pluralize",
    "decline_noun",
    "make_diminutive",
    "make_augmentative",
    "to_feminine",
    "to_masculine",
    "to_oblique",
    "extract_root",
    "conjugate",
    "conjugate_to_be",
    "conjunctive_participle",
    "agent_noun",
    "imperative",
    "SyntaxEngine",
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
]


