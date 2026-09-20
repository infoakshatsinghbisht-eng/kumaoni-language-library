import unittest
import kumaoni


class TestLexicon(unittest.TestCase):
    def test_lookup_exact(self):
        w = kumaoni.lookup("ईजा")
        self.assertIsNotNone(w)
        self.assertIn("mother", w.english)
        self.assertIn("माँ", w.hindi)

        # By Romanized
        w_rom = kumaoni.lookup("dajyu")
        self.assertIsNotNone(w_rom)
        self.assertEqual(w_rom.kumaoni, "दाज्यू")

    def test_search(self):
        results = kumaoni.search("water")
        self.assertTrue(any(r.kumaoni == "पाणि" for r in results))

        results_kin = kumaoni.search("brother")
        self.assertTrue(len(results_kin) > 0)

    def test_proverbs_and_riddles(self):
        all_provs = kumaoni.proverbs.list()
        self.assertGreater(len(all_provs), 0)
        p = kumaoni.proverbs.random()
        self.assertIn("kumaoni", p)

        all_riddles = kumaoni.riddles.list()
        self.assertGreater(len(all_riddles), 0)
        r = kumaoni.riddles.random()
        self.assertIn("riddle", r)

    def test_lexicon_scale(self):
        lex = kumaoni.get_lexicon()
        self.assertGreaterEqual(len(lex.words), 1000)


if __name__ == "__main__":
    unittest.main()
