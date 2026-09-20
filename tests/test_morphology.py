import unittest
import kumaoni


class TestMorphology(unittest.TestCase):
    def test_100k_words_coverage(self):
        """Verify the full morphological corpus generates over 100,000+ authentic Kumaoni word forms."""
        total = kumaoni.total_word_forms()
        self.assertGreaterEqual(total, 100_000, f"Expected at least 100,000 words, got {total}")

    def test_lemmatize_verbs(self):
        """Verify inflected verb forms correctly lemmatize to their base dictionary lemma."""
        self.assertEqual(kumaoni.lemmatize("खान्छू"), "खाण")
        self.assertEqual(kumaoni.lemmatize("जाँला"), "जाण")
        self.assertEqual(kumaoni.lemmatize("करूँलो"), "करण")
        self.assertEqual(kumaoni.lemmatize("बोलूँछ"), "बोलण")

    def test_lemmatize_nouns_and_postpositions(self):
        """Verify case-marked nouns and postpositional constructions lemmatize to base stems."""
        self.assertEqual(kumaoni.lemmatize("घरबटि"), "घर")
        self.assertEqual(kumaoni.lemmatize("ईजा कणी"), "ईजा")
        self.assertEqual(kumaoni.lemmatize("बाबु ले"), "बाबु")
        self.assertEqual(kumaoni.lemmatize("पहाड़बटी"), "पहाड़")

    def test_morphological_analysis(self):
        """Verify full grammatical feature extraction from inflected surface tokens."""
        analyses = kumaoni.analyze("खान्छू")
        self.assertGreater(len(analyses), 0)
        analysis = analyses[0]
        self.assertEqual(analysis.lemma, "खाण")
        self.assertEqual(analysis.pos, "verb_finite")
        self.assertEqual(analysis.tense, "present")
        self.assertEqual(analysis.person, 1)

        noun_analyses = kumaoni.analyze("घरबटि")
        self.assertGreater(len(noun_analyses), 0)
        noun_analysis = noun_analyses[0]
        self.assertEqual(noun_analysis.lemma, "घर")
        self.assertEqual(noun_analysis.case, "ablative")

    def test_dictionary_inflected_lookup(self):
        """Verify Lexicon.lookup seamlessly resolves inflected surface forms to their base definitions."""
        w_verb = kumaoni.lookup("खान्छू")
        self.assertIsNotNone(w_verb)
        self.assertEqual(w_verb.kumaoni, "खाण")
        self.assertIn("eat", w_verb.english.lower())

        w_noun = kumaoni.lookup("घरबटि")
        self.assertIsNotNone(w_noun)
        self.assertEqual(w_noun.kumaoni, "घर")
        self.assertIn("house", w_noun.english.lower())

    def test_paradigm_generation(self):
        """Verify paradigm generator produces rich morphological paradigms."""
        morph = kumaoni.KumaoniMorphology()
        verb_paradigms = morph.generate_verb_paradigm("खाण")
        self.assertGreater(len(verb_paradigms), 30)

        noun_paradigms = morph.generate_noun_paradigm("घर")
        self.assertGreater(len(noun_paradigms), 15)


if __name__ == "__main__":
    unittest.main()
