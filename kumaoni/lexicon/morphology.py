# -*- coding: utf-8 -*-
"""
Kumaoni Morphological Analyzer and Paradigm Generator
====================================================

Generates and analyzes 100,000+ full-form inflectional variants,
derived stems, case-marked nouns, verbal paradigms, causatives,
participles, agentives, diminutives, augmentatives, and dialectal cognates
from authentic Kumaoni lemmas.
"""

from typing import Dict, List, Set, Tuple, Optional, Any, Iterator
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class MorphAnalysis:
    lemma: str
    surface_form: str
    pos: str
    tense: Optional[str] = None
    aspect: Optional[str] = None
    mood: Optional[str] = None
    person: Optional[int] = None
    gender: Optional[str] = None
    number: Optional[str] = None
    case: Optional[str] = None
    voice: Optional[str] = None
    english_meaning: Optional[str] = None
    hindi_meaning: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class KumaoniMorphology:
    """
    Exhaustive morphological paradigm generator and analyzer for Kumaoni.
    """

    # --- Verbal Inflectional Suffixes ---
    PRES_ENDINGS = {
        (1, "m", "sg"): ["न्छू", "न्दू", "नू", "न् छू", "न् छुं"],
        (1, "f", "sg"): ["न्छी", "न्दी", "नी", "न् छी"],
        (1, "m", "pl"): ["न्छाँ", "न्दूँ", "न्यूँ", "न्छा", "न् छां", "न् छा"],
        (1, "f", "pl"): ["न्छीं", "न्दीं", "नीं", "न् छीं"],
        (2, "m", "sg"): ["न्छै", "न्दै", "नै", "न् छै"],
        (2, "f", "sg"): ["न्छी", "न्दी", "नी", "न् छी"],
        (2, "m", "pl"): ["न्छा", "न्दा", "ना", "न् छा"],
        (2, "f", "pl"): ["न्छा", "न्दीं", "नीं", "न् छा"],
        (3, "m", "sg"): ["न्छ", "न्द", "न", "न् छ", "न्"],
        (3, "f", "sg"): ["न्छि", "न्दि", "नि", "न्छी", "न् छि"],
        (3, "m", "pl"): ["न्छा", "न्दन", "नन", "न", "न् छन"],
        (3, "f", "pl"): ["न्छां", "न्दीन", "नीन", "न् छीन"],
    }

    PAST_ENDINGS = {
        (1, "m", "sg"): ["यूँ", "ओ", "यो", "उं", "छियूँ", "छ्यूँ"],
        (1, "f", "sg"): ["ई", "यी", "इ", "छी", "छियी"],
        (1, "m", "pl"): ["याँ", "या", "यूं", "छियाँ", "छ्याँ"],
        (1, "f", "pl"): ["यीं", "ईं", "छीन", "छियों"],
        (2, "m", "sg"): ["ये", "ए", "या", "छिये", "छि"],
        (2, "f", "sg"): ["ई", "यी", "इ", "छी"],
        (2, "m", "pl"): ["या", "आ", "छिया"],
        (2, "f", "pl"): ["ईं", "यीं", "छीन"],
        (3, "m", "sg"): ["यो", "ओ", "या", "छियो", "थो"],
        (3, "f", "sg"): ["ई", "यी", "इ", "ए", "छि", "थी"],
        (3, "m", "pl"): ["या", "ए", "छिया", "था"],
        (3, "f", "pl"): ["ईं", "यीं", "छिन", "थीन"],
    }

    FUT_ENDINGS = {
        (1, "m", "sg"): ["लूँ", "लो", "लूं", "हूँलो", "होलूँ"],
        (1, "f", "sg"): ["ली", "लि", "हूँली", "होली"],
        (1, "m", "pl"): ["लाँ", "ला", "ँला", "हूँला", "होला"],
        (1, "f", "pl"): ["लीं", "लिं", "हूँलीं", "होलीं"],
        (2, "m", "sg"): ["ले", "ला", "होले"],
        (2, "f", "sg"): ["ली", "लि", "होली"],
        (2, "m", "pl"): ["ला", "होला"],
        (2, "f", "pl"): ["लीं", "लिं", "होलीं"],
        (3, "m", "sg"): ["लो", "ल", "होलो", "होल"],
        (3, "f", "sg"): ["ली", "लि", "होली"],
        (3, "m", "pl"): ["ला", "लन", "होला", "होलन"],
        (3, "f", "pl"): ["लीं", "लिन", "होलीं", "होलिन"],
    }

    CONT_STEMS = [
        "रैछ", "रैछू", "रैछा", "रैछी", "रैछन", "रैछि",
        "रयो", "रई", "रया", "रौलो", "रौली", "रौला",
        "रै", "रैबेर", "रैछिया", "रैछियो", "रैछिन"
    ]

    IMP_ENDINGS = {
        ("informal", "sg"): ["", "अ", "इ"],
        ("polite", "sg"): ["या", "इए", "इया", "ओ"],
        ("honorific", "pl"): ["या", "ओ", "इयो", "इबेर", "इयाला"],
        ("future_obligation", "sg"): ["ये", "इय", "इयो"],
    }

    PARTICIPLE_SUFFIXES = [
        ("conjunctive", ["बेर", "इबेर", "ई", "कन", "ले", "ईबेर", "इ"]),
        ("agentive", ["ण्या", "वार", "हार", "वाल", "वाला", "वाली", "वाले", "वालि"]),
        ("infinitive_oblique", ["ण", "न", "णा", "ना", "णक", "नक", "णहुणि", "नहुणि", "णकणि", "नकणि", "णबटि", "नबटि", "णम", "नम"]),
        ("conditional", ["नेम", "न्दो", "न्दायि", "णम", "नेपर", "णपर"]),
        ("habitual_adj", ["ण्या", "निहार", "न्दार", "णे"]),
    ]

    CASE_CLITICS = [
        ("direct_nom", [""]),
        ("ergative_agentive", ["ले", "ल"]),
        ("dative_accusative", ["कणी", "कण", "कै", "कें", "हुणि", "हूँ", "काणि", "हुँ"]),
        ("instrumental", ["ले", "जरियाल", "हातै", "बटी", "द्वार"]),
        ("ablative", ["बटि", "बटी", "हैं", "थैं", "बट", "बाटी", "है"]),
        ("genitive_m_sg", ["को", "क"]),
        ("genitive_f_sg", ["की", "कि"]),
        ("genitive_pl", ["का", "काँ", "का"]),
        ("locative_in", ["म", "में", "भितर", "माँ", "माँझ"]),
        ("locative_on", ["पं", "पर", "मायि", "मथि", "मलि", "माथि"]),
        ("locative_under", ["मुणि", "तलि", "निसि", "तळ"]),
        ("sociative", ["दगड़", "दगड़े", "साथ", "संग", "सती"]),
        ("terminative", ["तक", "तलक", "सम्म", "कणि", "धरि"]),
        ("emphatic", ["इ", "ले", "रगै", "त", "हि"]),
    ]

    @classmethod
    def extract_root(cls, verb: str) -> str:
        if not verb:
            return ""
        if verb.endswith("ण") or verb.endswith("न"):
            return verb[:-1]
        return verb

    @classmethod
    def generate_verb_paradigms(cls, infinitive: str, base_english: str = "", base_hindi: str = "") -> List[MorphAnalysis]:
        forms: List[MorphAnalysis] = []
        root = cls.extract_root(infinitive)
        if not root:
            return forms

        forms.append(MorphAnalysis(
            lemma=infinitive,
            surface_form=infinitive,
            pos="verb_infinitive",
            english_meaning=f"to {base_english}" if base_english else None,
            hindi_meaning=base_hindi or None
        ))

        # 2. Present Tense (Finite)
        for (person, gender, number), endings in cls.PRES_ENDINGS.items():
            for end in endings:
                surf = root + end
                forms.append(MorphAnalysis(
                    lemma=infinitive,
                    surface_form=surf,
                    pos="verb_finite",
                    tense="present",
                    person=person,
                    gender=gender,
                    number=number,
                    english_meaning=f"{base_english} (present {person}{number})" if base_english else None,
                    hindi_meaning=base_hindi
                ))
                # Support contracted present continuous / habitual with nasalized stem (e.g. पढूँछ, करूँछ)
                if not root.endswith(("ा", "ी", "ू", "ो", "े")):
                    forms.append(MorphAnalysis(
                        lemma=infinitive,
                        surface_form=root + "ूँ" + end.lstrip("न्"),
                        pos="verb_finite",
                        tense="present",
                        person=person,
                        gender=gender,
                        number=number,
                        english_meaning=f"{base_english} (present {person}{number})" if base_english else None,
                        hindi_meaning=base_hindi
                    ))

        # 3. Past Tense (Finite)
        for (person, gender, number), endings in cls.PAST_ENDINGS.items():
            for end in endings:
                if root in ("जा", "जाण"):
                    if end in ("यूँ", "उं", "छियूँ", "छ्यूँ"):
                        surf = "ग्यूँ"
                    elif end in ("याँ", "या", "यूं", "छियाँ", "छ्याँ"):
                        surf = "ग्याँ"
                    elif end in ("यो", "ओ", "छियो", "थो"):
                        surf = "गयो"
                    elif end in ("ई", "यी", "इ", "छी", "छियी", "थी"):
                        surf = "गै"
                    else:
                        surf = "ग" + end
                elif root in ("खा", "खाण"):
                    surf = "खा" + end
                elif root in ("कर", "करण", "करन"):
                    surf = "कर्" + end if end.startswith("य") else "कर" + end
                elif root in ("दि", "दिण"):
                    surf = "दी" + end if end.startswith("य") else "दि" + end
                elif root in ("लि", "लिण"):
                    surf = "ली" + end if end.startswith("य") else "लि" + end
                else:
                    surf = root + end
                forms.append(MorphAnalysis(
                    lemma=infinitive,
                    surface_form=surf,
                    pos="verb_finite",
                    tense="past",
                    person=person,
                    gender=gender,
                    number=number,
                    english_meaning=f"{base_english} (past {person}{number})" if base_english else None,
                    hindi_meaning=base_hindi
                ))

        # 4. Future Tense (Finite)
        for (person, gender, number), endings in cls.FUT_ENDINGS.items():
            for end in endings:
                # Direct stem
                surf = root + end
                forms.append(MorphAnalysis(
                    lemma=infinitive,
                    surface_form=surf,
                    pos="verb_finite",
                    tense="future",
                    person=person,
                    gender=gender,
                    number=number,
                    english_meaning=f"will {base_english}" if base_english else None,
                    hindi_meaning=base_hindi
                ))
                # Nasalized / vocalic future stems for consonant roots (e.g. कर -> करूँलो, करूलो, करूँला)
                if not root.endswith(("ा", "ी", "ू", "ो", "े")):
                    forms.append(MorphAnalysis(
                        lemma=infinitive,
                        surface_form=root + "ूँ" + end,
                        pos="verb_finite",
                        tense="future",
                        person=person,
                        gender=gender,
                        number=number,
                        english_meaning=f"will {base_english}" if base_english else None,
                        hindi_meaning=base_hindi
                    ))
                    forms.append(MorphAnalysis(
                        lemma=infinitive,
                        surface_form=root + "ू" + end,
                        pos="verb_finite",
                        tense="future",
                        person=person,
                        gender=gender,
                        number=number,
                        english_meaning=f"will {base_english}" if base_english else None,
                        hindi_meaning=base_hindi
                    ))
                elif root.endswith("ा"):
                    # For roots in 'ा' (e.g. जा, खा): जाँलो, जाँला, खाँलो, खाँला
                    forms.append(MorphAnalysis(
                        lemma=infinitive,
                        surface_form=root[:-1] + "ाँ" + end,
                        pos="verb_finite",
                        tense="future",
                        person=person,
                        gender=gender,
                        number=number,
                        english_meaning=f"will {base_english}" if base_english else None,
                        hindi_meaning=base_hindi
                    ))

        # 5. Continuous Aspect Stems
        for cont in cls.CONT_STEMS:
            forms.append(MorphAnalysis(
                lemma=infinitive,
                surface_form=f"{root} {cont}",
                pos="verb_continuous",
                aspect="continuous",
                english_meaning=f"is {base_english}-ing" if base_english else None,
                hindi_meaning=base_hindi
            ))

        # 6. Imperatives
        for (mood_type, num), endings in cls.IMP_ENDINGS.items():
            for end in endings:
                surf = root + end
                if surf:
                    forms.append(MorphAnalysis(
                        lemma=infinitive,
                        surface_form=surf,
                        pos="verb_imperative",
                        mood=mood_type,
                        number=num,
                        english_meaning=f"{base_english}!" if base_english else None,
                        hindi_meaning=base_hindi
                    ))

        # 7. Participles & Non-Finite Forms
        for part_type, suffixes in cls.PARTICIPLE_SUFFIXES:
            for sfx in suffixes:
                if sfx.startswith("इ") or sfx.startswith("ई"):
                    surf = root + sfx
                elif sfx in ("बेर", "कन", "ले"):
                    surf = root + "ई" + sfx if not root.endswith("ई") else root + sfx
                else:
                    surf = root + sfx
                forms.append(MorphAnalysis(
                    lemma=infinitive,
                    surface_form=surf,
                    pos=f"verb_{part_type}",
                    aspect=part_type,
                    english_meaning=f"{base_english} ({part_type})" if base_english else None,
                    hindi_meaning=base_hindi
                ))

        # 8. Causative Grade 1 & Grade 2
        c1_stem = root + "ाण" if not root.endswith("ा") else root[:-1] + "िलाण"
        c2_stem = root + "वाण" if not root.endswith("ा") else root[:-1] + "िलवाण"
        
        forms.append(MorphAnalysis(
            lemma=infinitive,
            surface_form=c1_stem,
            pos="verb_causative_1",
            voice="causative_1",
            english_meaning=f"to cause to {base_english}" if base_english else None,
            hindi_meaning=base_hindi
        ))
        forms.append(MorphAnalysis(
            lemma=infinitive,
            surface_form=c2_stem,
            pos="verb_causative_2",
            voice="causative_2",
            english_meaning=f"to have someone {base_english}" if base_english else None,
            hindi_meaning=base_hindi
        ))

        return forms

    @classmethod
    def generate_noun_paradigms(cls, noun: str, base_english: str = "", base_hindi: str = "") -> List[MorphAnalysis]:
        forms: List[MorphAnalysis] = []
        if not noun:
            return forms

        # 1. Base Direct Singular
        forms.append(MorphAnalysis(
            lemma=noun,
            surface_form=noun,
            pos="noun",
            case="direct_nom",
            number="sg",
            english_meaning=base_english or None,
            hindi_meaning=base_hindi or None
        ))

        # 2. Plural Form
        pl_form = noun
        if noun.endswith("ो"):
            pl_form = noun[:-1] + "ा"
        elif noun.endswith("ी") or noun.endswith("ि"):
            pl_form = noun[:-1] + "ियन"
        else:
            pl_form = noun + "न"

        forms.append(MorphAnalysis(
            lemma=noun,
            surface_form=pl_form,
            pos="noun",
            case="direct_nom",
            number="pl",
            english_meaning=f"{base_english} (plural)" if base_english else None,
            hindi_meaning=base_hindi
        ))

        # 3. Oblique Base (Singular & Plural)
        obl_sg = noun[:-1] + "ा" if noun.endswith("ो") else noun
        obl_pl = noun[:-1] + "ान" if noun.endswith(("ा", "ो")) else (noun[:-1] + "ियन" if noun.endswith(("ी", "ि")) else noun + "न")

        # 4. Attach all Case Postpositions to Singular & Plural (both bound and spaced)
        for case_name, clitics in cls.CASE_CLITICS:
            for cl in clitics:
                if not cl:
                    continue
                
                # Sg forms (both bound and spaced)
                forms.append(MorphAnalysis(
                    lemma=noun,
                    surface_form=f"{obl_sg} {cl}",
                    pos="noun_declined",
                    case=case_name,
                    number="sg",
                    english_meaning=f"{base_english} ({case_name})" if base_english else None,
                    hindi_meaning=base_hindi
                ))
                forms.append(MorphAnalysis(
                    lemma=noun,
                    surface_form=f"{obl_sg}{cl}",
                    pos="noun_declined",
                    case=case_name,
                    number="sg",
                    english_meaning=f"{base_english} ({case_name})" if base_english else None,
                    hindi_meaning=base_hindi
                ))

                # Pl forms (both bound and spaced)
                forms.append(MorphAnalysis(
                    lemma=noun,
                    surface_form=f"{obl_pl} {cl}",
                    pos="noun_declined",
                    case=case_name,
                    number="pl",
                    english_meaning=f"{base_english} (pl {case_name})" if base_english else None,
                    hindi_meaning=base_hindi
                ))
                forms.append(MorphAnalysis(
                    lemma=noun,
                    surface_form=f"{obl_pl}{cl}",
                    pos="noun_declined",
                    case=case_name,
                    number="pl",
                    english_meaning=f"{base_english} (pl {case_name})" if base_english else None,
                    hindi_meaning=base_hindi
                ))

        # 5. Diminutives
        if noun.endswith(("ो", "ा")):
            dim = noun[:-1] + "ी"
            forms.append(MorphAnalysis(
                lemma=noun,
                surface_form=dim,
                pos="noun_diminutive",
                english_meaning=f"small/beloved {base_english}" if base_english else None,
                hindi_meaning=base_hindi
            ))
        elif noun.endswith(("ड़", "ट", "ल")):
            dim = noun + "ि"
            forms.append(MorphAnalysis(
                lemma=noun,
                surface_form=dim,
                pos="noun_diminutive",
                english_meaning=f"small/beloved {base_english}" if base_english else None,
                hindi_meaning=base_hindi
            ))

        # 6. Reduplicative Echo Words (e.g. भात-शात, पाणि-शाणि, घर-शर)
        first_char = noun[0]
        rest = noun[1:]
        echo_prefix = "वा" if first_char in ("श", "स", "ष") else "शा"
        echo_tail = echo_prefix + rest if len(noun) > 1 else echo_prefix
        
        # S-echo (e.g. घर -> शर, भात -> शात)
        if len(noun) >= 2:
            s_echo = "श" + noun[1:]
            forms.append(MorphAnalysis(lemma=noun, surface_form=f"{noun}-{s_echo}", pos="noun_echo", english_meaning=f"{base_english} and such", hindi_meaning=base_hindi))
            forms.append(MorphAnalysis(lemma=noun, surface_form=f"{noun} {s_echo}", pos="noun_echo", english_meaning=f"{base_english} and such", hindi_meaning=base_hindi))
            
            sha_echo = "शा" + noun[1:]
            forms.append(MorphAnalysis(lemma=noun, surface_form=f"{noun}-{sha_echo}", pos="noun_echo", english_meaning=f"{base_english} and such", hindi_meaning=base_hindi))
            forms.append(MorphAnalysis(lemma=noun, surface_form=f"{noun} {sha_echo}", pos="noun_echo", english_meaning=f"{base_english} and such", hindi_meaning=base_hindi))

        return forms

    @classmethod
    def generate_adjective_paradigms(cls, adj: str, base_english: str = "", base_hindi: str = "") -> List[MorphAnalysis]:
        forms: List[MorphAnalysis] = []
        if not adj:
            return forms

        forms.append(MorphAnalysis(lemma=adj, surface_form=adj, pos="adjective", gender="m", number="sg", english_meaning=base_english, hindi_meaning=base_hindi))

        if adj.endswith("ो"):
            forms.append(MorphAnalysis(lemma=adj, surface_form=adj[:-1] + "ा", pos="adjective", gender="m", number="pl", english_meaning=base_english, hindi_meaning=base_hindi))
            forms.append(MorphAnalysis(lemma=adj, surface_form=adj[:-1] + "ी", pos="adjective", gender="f", number="sg", english_meaning=base_english, hindi_meaning=base_hindi))
            forms.append(MorphAnalysis(lemma=adj, surface_form=adj[:-1] + "ीं", pos="adjective", gender="f", number="pl", english_meaning=base_english, hindi_meaning=base_hindi))

        forms.append(MorphAnalysis(lemma=adj, surface_form=adj + "इ", pos="adjective_emphatic", english_meaning=f"very/strictly {base_english}" if base_english else None, hindi_meaning=base_hindi))

        return forms

    # Singular aliases
    generate_verb_paradigm = generate_verb_paradigms
    generate_noun_paradigm = generate_noun_paradigms
    generate_adjective_paradigm = generate_adjective_paradigms


class FullFormCorpus:
    """
    High-capacity dictionary store indexing 100,000+ generated and analyzed wordforms.
    Provides sub-millisecond lookup and lemmatization.
    """
    _instance: Optional["FullFormCorpus"] = None

    def __init__(self):
        self._surface_index: Dict[str, List[MorphAnalysis]] = {}
        self._total_forms_count: int = 0
        self._is_built: bool = False

    @classmethod
    def get_instance(cls) -> "FullFormCorpus":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def build_corpus(self, raw_words: List[Dict[str, Any]]) -> int:
        if self._is_built:
            return self._total_forms_count

        seen_surfaces: Set[str] = set()

        for item in raw_words:
            k = item.get("kumaoni", "").strip()
            en = item.get("english", "").strip()
            hi = item.get("hindi", "").strip()
            pos = item.get("pos", "noun").lower()
            cat = item.get("category", "").lower()

            if not k:
                continue

            analyses: List[MorphAnalysis] = []
            if "verb" in pos or "verb" in cat:
                analyses = KumaoniMorphology.generate_verb_paradigms(k, en, hi)
            elif "adj" in pos or "adj" in cat or pos in ("quality", "taste") or cat in ("quality", "taste"):
                analyses = KumaoniMorphology.generate_adjective_paradigms(k, en, hi)
            elif pos in ("adverb", "conjunction", "interjection", "particle", "postposition") and cat not in ("food", "tool", "house", "nature", "animals"):
                analyses = [
                    MorphAnalysis(lemma=k, surface_form=k, pos=pos, english_meaning=en, hindi_meaning=hi),
                    MorphAnalysis(lemma=k, surface_form=k + "इ", pos=f"{pos}_emphatic", english_meaning=en, hindi_meaning=hi)
                ]
            else:
                analyses = KumaoniMorphology.generate_noun_paradigms(k, en, hi)

            for ma in analyses:
                surf = ma.surface_form.strip()
                if not surf:
                    continue
                self._surface_index.setdefault(surf, []).append(ma)
                seen_surfaces.add(surf)
                
                # Also index non-nukta variant if contains nukta
                if "\u093c" in surf:
                    non_nukta = surf.replace("\u093c", "")
                    self._surface_index.setdefault(non_nukta, []).append(ma)
                    seen_surfaces.add(non_nukta)

        self._total_forms_count = len(seen_surfaces)
        self._is_built = True
        return self._total_forms_count

    def analyze(self, word: str) -> List[MorphAnalysis]:
        if not word:
            return []
        w = word.strip()
        if w in self._surface_index:
            return self._surface_index[w]
        # Check without nukta
        w_no_nukta = w.replace("\u093c", "")
        if w_no_nukta in self._surface_index:
            return self._surface_index[w_no_nukta]
        return []

    def lemmatize(self, word: str) -> str:
        res = self.analyze(word)
        if res:
            return res[0].lemma
        return word.strip()

    def contains(self, word: str) -> bool:
        return word.strip() in self._surface_index

    def total_forms(self) -> int:
        return self._total_forms_count
