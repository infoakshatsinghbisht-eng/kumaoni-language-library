import unittest
import kumaoni
from kumaoni.constants import Tense, Gender, GrammaticalNumber


class TestGrammar(unittest.TestCase):
    def test_extract_root(self):
        self.assertEqual(kumaoni.extract_root("खाण"), "खा")
        self.assertEqual(kumaoni.extract_root("जाण"), "जा")
        self.assertEqual(kumaoni.extract_root("करन"), "कर")

    def test_conjugate_present(self):
        self.assertEqual(kumaoni.conjugate("खाण", tense=Tense.PRESENT, person=1), "खान्छू")
        self.assertEqual(kumaoni.conjugate("खाण", tense=Tense.PRESENT, person=3), "खान्छ")
        self.assertEqual(kumaoni.conjugate("जाण", tense=Tense.PRESENT, person=1), "जान्छू")

    def test_conjugate_past(self):
        # Irregular past for जाण
        self.assertEqual(kumaoni.conjugate("जाण", tense=Tense.PAST, person=1, gender=Gender.MASCULINE), "ग्यूँ")
        self.assertEqual(kumaoni.conjugate("जाण", tense=Tense.PAST, person=3, gender=Gender.MASCULINE), "गयो")
        self.assertEqual(kumaoni.conjugate("जाण", tense=Tense.PAST, person=3, gender=Gender.FEMININE), "गै")

    def test_conjugate_to_be(self):
        self.assertEqual(kumaoni.conjugate_to_be(Tense.PRESENT, person=1), "छूँ")
        self.assertEqual(kumaoni.conjugate_to_be(Tense.PRESENT, person=3), "छ")
        self.assertEqual(kumaoni.conjugate_to_be(Tense.PAST, person=3, gender=Gender.MASCULINE), "थो")
        self.assertEqual(kumaoni.conjugate_to_be(Tense.PAST, person=3, gender=Gender.FEMININE), "थी")

    def test_noun_pluralization(self):
        self.assertEqual(kumaoni.pluralize("घ्वड़ो"), "घ्वड़ा")
        self.assertEqual(kumaoni.pluralize("चेलि"), "चेलियन")

    def test_noun_transformations(self):
        # Diminutives
        self.assertEqual(kumaoni.make_diminutive("डाला"), "डाली")
        self.assertEqual(kumaoni.make_diminutive("कूड़"), "कूड़ि")

        # Augmentatives
        self.assertEqual(kumaoni.make_augmentative("कूड़ि"), "कूड़")
        self.assertEqual(kumaoni.make_augmentative("डाली"), "डाला")

        # Gender conversion
        self.assertEqual(kumaoni.to_feminine("चेलो"), "चेली")
        self.assertEqual(kumaoni.to_masculine("चेली"), "चेलो")

        # Oblique stems
        self.assertEqual(kumaoni.to_oblique("चेलो"), "चेला")
        self.assertEqual(kumaoni.to_oblique("घर", is_plural=True), "घरन")

    def test_postpositions_and_cases(self):
        self.assertEqual(kumaoni.attach_case("राम", "nominative_agentive"), "रामले")
        self.assertEqual(kumaoni.attach_case("घर", "ablative"), "घर बटि")
        self.assertEqual(kumaoni.attach_case("इजा", "sociative_comitative"), "इजा दगड़")
        self.assertEqual(kumaoni.attach_case("सांझ", "terminative"), "सांझ तक")
        self.assertEqual(kumaoni.attach_case("डाँड़ा", "locative_superior"), "डाँड़ा मायि")
        self.assertEqual(kumaoni.attach_case("बोट", "locative_inferior"), "बोट मुणि")

    def test_participles_and_morphology(self):
        # Conjunctive participles (-बेर / -इबेर)
        self.assertEqual(kumaoni.conjunctive_participle("खाण"), "खाईबेर")
        self.assertEqual(kumaoni.conjunctive_participle("जाण"), "जाईबेर")
        self.assertEqual(kumaoni.conjunctive_participle("करण"), "करिबेर")

        # Agent nouns (-ण्या)
        self.assertEqual(kumaoni.agent_noun("खाण"), "खाण्या")
        self.assertEqual(kumaoni.agent_noun("गाण"), "गाण्या")
        self.assertEqual(kumaoni.agent_noun("बोलण"), "बोलण्या")

        # Imperatives
        self.assertEqual(kumaoni.imperative("खाण", polite=False), "खा")
        self.assertEqual(kumaoni.imperative("खाण", polite=True), "खाया")
        self.assertEqual(kumaoni.imperative("औण", polite=True), "आया")

    def test_syntax_and_sentence_formation(self):
        # Causatives
        self.assertEqual(kumaoni.causative("खाण", degree=1), "खिलाण")
        self.assertEqual(kumaoni.causative("करण", degree=1), "करौण")
        self.assertEqual(kumaoni.causative("करण", degree=2), "करवाण")

        # Passives
        self.assertEqual(kumaoni.passive("करण", Tense.PRESENT), "कर्यो जान्छ")
        self.assertEqual(kumaoni.passive("खाण", Tense.PRESENT), "खायो जान्छ")


        # Medio-passive inability (-बटि)
        self.assertIn("नी जाँछ", kumaoni.medio_passive_inability("मैं", "हिंण"))

        # Compound verbs
        self.assertEqual(kumaoni.compound_verb("खाण", "हाल्ण"), "खाईहाल्ण")
        self.assertEqual(kumaoni.compound_verb("करण", "दिण"), "करिदिण")

        # Echo words
        self.assertEqual(kumaoni.echo_word("पाणि"), "पाणि-शाणि")
        self.assertEqual(kumaoni.echo_word("भात"), "भात-शात")
        self.assertEqual(kumaoni.echo_word("चाय"), "चाय-वाय")

        # SOV sentence builder
        sent = kumaoni.build_sentence(
            subject="राम",
            direct_object="भात",
            verb="खाण",
            tense=Tense.PRESENT,
            person=3,
        )
        self.assertEqual(sent, "राम भात खान्छ।")

        # Conditional sentences
        cond = kumaoni.conditional("बरखा होली", "हम घर म रौला")
        self.assertEqual(cond, "जै बरखा होली, त हम घर म रौला।")

    def test_advanced_syntax_and_modals(self):
        # Relative-Correlative
        rel = kumaoni.relative_correlative("मेहनत करलो", "फल पालो", marker_type="who")
        self.assertEqual(rel, "जो मेहनत करलो, सो फल पालो।")

        rel_loc = kumaoni.relative_correlative("पाणि छ", "जीवन छ", marker_type="where")
        self.assertEqual(rel_loc, "जहाँ पाणि छ, तहाँ जीवन छ।")

        # Prohibitive imperative (झनि)
        self.assertEqual(kumaoni.prohibitive("जाण", polite=True), "झनि जाया")
        self.assertEqual(kumaoni.prohibitive("करण", polite=False), "झनि कर")

        # Modal Ability (सकण)
        self.assertIn("सकन्छू", kumaoni.modal_ability("मैं", "हिंण"))

        # Modal Obligation (चाही / पडलो)
        self.assertIn("चाही", kumaoni.modal_obligation("तुम", "काम करण"))
        self.assertIn("पडलो", kumaoni.modal_obligation("मैं", "जाण", strong=True))

        # Modal Desiderative (चाण)
        self.assertIn("चान्छू", kumaoni.modal_desiderative("मैं", "भात खाण"))

        # Interrogative sentences
        q = kumaoni.interrogative_sentence("कहाँ", subject="अस्पताल", verb="छ")
        self.assertEqual(q, "अस्पताल कहाँ छ?")


if __name__ == "__main__":
    unittest.main()


