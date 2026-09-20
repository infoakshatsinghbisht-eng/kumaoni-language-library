"""
Kumaoni Syntax and Sentence Formation Engine.
Based on D.D. Sharma's 'The Formation of Kumauni Language' and Grierson's Central Pahari survey.

Features:
- SOV (Subject-Object-Verb) clause generation
- Causative verb derivation (1st & 2nd causatives)
- Passive & Medio-Passive (inability with '-बटि') constructions
- Compound / Vector verbs (-हाल्ण, -दिण, -लिण, -रूण, -बैठण)
- Conditional clauses (अगर / जै ... त / तबे)
- Echo words and Reduplication (पाणि-वाणी, भात-शात, धिरै-धिरै)
"""

from typing import Dict, List, Optional, Tuple, Union
from kumaoni.constants import Tense, Gender, GrammaticalNumber
from kumaoni.grammar.verbs import extract_root, conjugate, conjugate_to_be, conjunctive_participle
from kumaoni.grammar.postpositions import attach_case


class SyntaxEngine:
    """
    Engine for generating grammatically accurate Kumaoni sentences,
    passive transformations, causative shifts, and complex clauses.
    """

    @staticmethod
    def causative(verb: str, degree: int = 1) -> str:
        """
        Derives the 1st or 2nd causative form of a Kumaoni verb.
        E.g.:
        causative('करण', 1) -> 'करौण' (to cause to do / make someone do)
        causative('करण', 2) -> 'करवाण' (to get done through another)
        causative('खाण', 1) -> 'खिलाण' (to feed)
        causative('पडण', 1) -> 'पढाण' (to teach / cause to read)
        causative('बोलण', 1) -> 'बुलौण' (to call / cause to speak)
        """
        verb_clean = verb.strip()
        
        # Irregular causatives
        irreg_1 = {
            "खाण": "खिलाण",
            "पिण": "पिलाण",
            "जाण": "भेजण",
            "औण": "बुलौण",
            "बोलण": "बुलौण",
            "देखण": "दिखाण",
            "पडण": "पढाण",
            "लिकण": "लिकाण",
            "सुणण": "सुणाण",
            "सुतण": "सुताण",
            "बैठण": "बिठाण",
            "धोण": "धुवाण",
        }
        irreg_2 = {
            "खाण": "खिलवाण",
            "पिण": "पिलवाण",
            "करण": "करवाण",
            "पडण": "पढवाण",
            "लिकण": "लिखवाण",
            "बणौण": "बणवाण",
            "धोण": "धुलवाण",
        }

        if degree == 1:
            if verb_clean in irreg_1:
                return irreg_1[verb_clean]
            root = extract_root(verb_clean)
            return f"{root}ौण"
        else:  # degree == 2
            if verb_clean in irreg_2:
                return irreg_2[verb_clean]
            root = extract_root(verb_clean)
            return f"{root}वाण"

    @staticmethod
    def passive(
        verb: str,
        tense: Tense = Tense.PRESENT,
        person: int = 3,
        gender: Gender = Gender.MASCULINE,
        number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    ) -> str:
        """
        Forms a passive voice predicate (Main Verb Past Participle + 'जाण' auxiliary).
        E.g.:
        passive('करण', Tense.PRESENT) -> 'कियो जाँछ' (is done)
        passive('खाण', Tense.PRESENT) -> 'खायो जाँछ' (is eaten)
        passive('देखण', Tense.PAST) -> 'देख्यो ग्यो' (was seen)
        """
        verb_clean = verb.strip()
        past_participle = conjugate(verb_clean, tense=Tense.PAST, person=3, gender=gender, number=number)
        aux_go = conjugate("जाण", tense=tense, person=person, gender=gender, number=number)
        return f"{past_participle} {aux_go}"

    @staticmethod
    def medio_passive_inability(subject: str, verb: str, gender: Gender = Gender.MASCULINE) -> str:
        """
        Forms the classic Kumaoni medio-passive inability sentence with '-बटि' marker.
        E.g.:
        medio_passive_inability('मैं', 'हिंण') -> 'मैंबटि हिंड्यो नी जाँछ।' (I am unable to walk)
        medio_passive_inability('ऊ', 'खाण') -> 'उकबटि खायो नी जाँछ।' (He is unable to eat)
        """
        sub_with_case = attach_case(subject, "ablative") if subject not in ("मैं", "ऊ", "तुम", "हम") else (
            "मैंबटि" if subject == "मैं" else (
                "उकबटि" if subject == "ऊ" else (
                    "तुमबटि" if subject == "तुम" else "हमबटि"
                )
            )
        )
        past_verb = conjugate(verb, tense=Tense.PAST, person=3, gender=gender, number=GrammaticalNumber.SINGULAR)
        return f"{sub_with_case} {past_verb} नी जाँछ।"

    @staticmethod
    def compound_verb(verb: str, vector: str = "हाल्ण") -> str:
        """
        Forms a compound (complex) verb combining conjunctive base with a vector verb.
        Vectors:
        - 'हाल्ण' (completive / sudden action, e.g. खाईहाल्ण - to finish eating up)
        - 'दिण' (benefactive, e.g. करिदिण - to do for someone, बताईदिण - to tell someone)
        - 'लिण' (reflexive, e.g. सोचीलिण - to think to oneself)
        - 'रूण' (continuous, e.g. लागीरूण - to keep ongoing)
        """
        root = extract_root(verb)
        base = f"{root}ि" if not root.endswith(("ा", "ो", "ू", "ौ")) else f"{root}ई"
        return f"{base}{vector}"


    @staticmethod
    def echo_word(word: str) -> str:
        """
        Generates traditional Kumaoni reduplicated echo word (e.g. पाणि-वाणी, भात-शात, चाय-वाय).
        """
        w = word.strip()
        if not w:
            return w
        # Standard pahari echo initial replacement
        first_char = w[0]
        if first_char in ("प", "ब", "भ", "म"):
            echo_part = "श" + w[1:] if len(w) > 1 else "शात"
        else:
            echo_part = "व" + w[1:] if len(w) > 1 else "वात"
        return f"{w}-{echo_part}"

    @staticmethod
    def build_sentence(
        subject: Optional[str] = None,
        direct_object: Optional[str] = None,
        indirect_object: Optional[str] = None,
        verb: str = "करण",
        adverb: Optional[str] = None,
        tense: Tense = Tense.PRESENT,
        person: int = 3,
        gender: Gender = Gender.MASCULINE,
        number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
        negation: bool = False,
        honorific: bool = False,
    ) -> str:
        """
        Constructs a grammatically aligned SOV Kumaoni sentence.
        Order: [Subject] [Indirect Object + कणी] [Time/Adverb] [Direct Object] [Negation (नी)] [Verb]
        """
        tokens: List[str] = []

        # 1. Subject (with ergative '-ले' in transitive past)
        if subject:
            is_transitive_past = (tense == Tense.PAST and verb not in ("जाण", "औण", "रूण", "सुतण", "बैठण", "हिंण", "धाण", "हाँसण", "रोण"))
            if is_transitive_past and subject not in ("मैं", "तू"):
                sub_tok = attach_case(subject, "nominative_agentive")
            elif is_transitive_past and subject == "मैं":
                sub_tok = "मैंले"
            elif is_transitive_past and subject == "तू":
                sub_tok = "तैंले"
            else:
                sub_tok = subject
            tokens.append(sub_tok)

        # 2. Indirect object (with dative '-कणी')
        if indirect_object:
            io_tok = attach_case(indirect_object, "dative")
            tokens.append(io_tok)

        # 3. Adverb / Time
        if adverb:
            tokens.append(adverb)

        # 4. Direct Object
        if direct_object:
            tokens.append(direct_object)

        # 5. Negation particle
        if negation:
            tokens.append("नी")

        # 6. Conjugated Verb
        verb_conj = conjugate(
            verb,
            tense=tense,
            person=person,
            gender=gender,
            number=number,
            honorific=honorific
        )
        tokens.append(verb_conj)

        sentence = " ".join(tokens) + "।"
        return sentence

    @staticmethod
    def conditional(condition_clause: str, result_clause: str) -> str:
        """
        Creates a conditional 'अगर / जै ... त' sentence.
        E.g.:
        conditional('बरखा होली', 'हम घर म रौला') -> 'जै बरखा होली, त हम घर म रौला।'
        """
        cond = condition_clause.strip().rstrip("।").rstrip(",")
        res = result_clause.strip().rstrip("।")
        return f"जै {cond}, त {res}।"

    @staticmethod
    def relative_correlative(rel_clause: str, cor_clause: str, marker_type: str = "who") -> str:
        """
        Constructs traditional Kumaoni relative-correlative complex sentences.
        marker_types:
        - 'who': 'जो ... सो' / 'जैले ... तैले' (e.g. 'जो मेहनत करलो, सो फल पालो')
        - 'where': 'जहाँ ... तहाँ' / 'जत्ता ... तत्ता' (e.g. 'जहाँ पाणि छ, तहाँ जीवन छ')
        - 'when': 'जब ... तब' / 'जब ... तबे' (e.g. 'जब घाम लागलो, तब हम जाँला')
        - 'how': 'जसो ... तसो' (e.g. 'जसो बोबा, तसो काटला')
        - 'quantity': 'जतुक ... ततुक' (e.g. 'जतुक चाही, ततुक लिया')
        """
        r = rel_clause.strip().rstrip("।").rstrip(",")
        c = cor_clause.strip().rstrip("।")

        pairs = {
            "who": ("जो", "सो"),
            "person": ("जो", "सो"),
            "agent": ("जैले", "तैले"),
            "where": ("जहाँ", "तहाँ"),
            "whither": ("जत्ता", "तत्ता"),
            "when": ("जब", "तबे"),
            "how": ("जसो", "तसो"),
            "quantity": ("जतुक", "ततुक"),
            "quality": ("जसो", "तसो"),
        }
        rel_mark, cor_mark = pairs.get(marker_type.lower(), ("जो", "सो"))
        return f"{rel_mark} {r}, {cor_mark} {c}।"

    @staticmethod
    def prohibitive(verb: str, polite: bool = True, plural: bool = False) -> str:
        """
        Forms the authentic Kumaoni negative imperative (prohibitive command) using 'झनि' / 'मत'.
        E.g.:
        prohibitive('जाण', polite=True) -> 'झनि जाया' (Please do not go)
        prohibitive('करण', polite=False) -> 'झनि कर' (Don't do it!)
        prohibitive('रोण', polite=True) -> 'झनि रोया' (Please don't cry)
        """
        root = extract_root(verb.strip())
        if not polite and not plural:
            return f"झनि {root}"
        end = "या" if root.endswith(("ा", "ो", "ू", "ौ")) else "िया"
        return f"झनि {root}{end}"

    @staticmethod
    def modal_ability(subject: str, verb: str, tense: Tense = Tense.PRESENT, person: int = 1, gender: Gender = Gender.MASCULINE, number: GrammaticalNumber = GrammaticalNumber.SINGULAR) -> str:
        """
        Constructs an ability clause with 'सकण' (can / to be able to).
        E.g.:
        modal_ability('मैं', 'हिंण', Tense.PRESENT, 1) -> 'मैं हिंडि सकूँछू।' (I can walk)
        modal_ability('ऊ', 'खाण', Tense.FUTURE, 3) -> 'ऊ खाई सकलो।' (He will be able to eat)
        """
        root = extract_root(verb.strip())
        inf_stem = f"{root}ई" if root.endswith(("ा", "ो", "ू", "ौ")) else f"{root}ि"
        sak_conj = conjugate("सकण", tense=tense, person=person, gender=gender, number=number)
        return f"{subject} {inf_stem} {sak_conj}।"

    @staticmethod
    def modal_obligation(subject: str, verb: str, strong: bool = False) -> str:
        """
        Constructs an obligation or necessity clause (should / must / have to).
        E.g.:
        modal_obligation('तुम', 'काम करण', strong=False) -> 'तुमकणी काम करण चाही।' (You should work)
        modal_obligation('मैं', 'जाण', strong=True) -> 'मैंकणी जाण पडलो।' (I will have to go)
        """
        sub_dative = attach_case(subject, "accusative_dative") if subject not in ("मैं", "तुम", "हम", "तू", "ऊ") else (
            "मैंकणी" if subject == "मैं" else (
                "तुमकणी" if subject == "तुम" else (
                    "हमकणी" if subject == "हम" else (
                        "तुकणी" if subject == "तू" else "उकणी"
                    )
                )
            )
        )
        if strong:
            return f"{sub_dative} {verb.strip()} पडलो।"
        return f"{sub_dative} {verb.strip()} चाही।"

    @staticmethod
    def modal_desiderative(subject: str, verb: str, tense: Tense = Tense.PRESENT, person: int = 1, gender: Gender = Gender.MASCULINE, number: GrammaticalNumber = GrammaticalNumber.SINGULAR) -> str:
        """
        Constructs a desiderative clause (want to / wish to) with 'चाण'.
        E.g.:
        modal_desiderative('मैं', 'भात खाण') -> 'मैं भात खाण चाँछू।' (I want to eat food)
        """
        cha_conj = conjugate("चाण", tense=tense, person=person, gender=gender, number=number)
        return f"{subject} {verb.strip()} {cha_conj}।"

    @staticmethod
    def interrogative_sentence(
        question_word: str,
        subject: Optional[str] = None,
        direct_object: Optional[str] = None,
        verb: str = "छ",
    ) -> str:
        """
        Constructs a standard Kumaoni interrogative question.
        E.g.:
        interrogative_sentence('कहाँ', subject='अस्पताल') -> 'अस्पताल कहाँ छ?'
        interrogative_sentence('क्या', subject='तुमार नाम') -> 'तुमार नाम क्या छ?'
        interrogative_sentence('कस', subject='तुम', verb='छू') -> 'तुम कस छू?'
        """
        tokens: List[str] = []
        if subject:
            tokens.append(subject)
        if direct_object:
            tokens.append(direct_object)
        tokens.append(question_word.strip())
        tokens.append(verb.strip())
        return " ".join(tokens) + "?"
