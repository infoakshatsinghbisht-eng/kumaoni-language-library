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
        self.assertGreaterEqual(len(lex.words), 2000)

    def test_extracted_words_lookup(self):
        w_simaar = kumaoni.lookup("सिमार")
        self.assertIsNotNone(w_simaar)
        self.assertIn("wetland", w_simaar.english)

        w_gadhera = kumaoni.lookup("गधेरा")
        self.assertIsNotNone(w_gadhera)
        self.assertIn("brook", w_gadhera.english)

        w_ukhal = kumaoni.lookup("उखल")
        self.assertIsNotNone(w_ukhal)
        self.assertIn("mortar", w_ukhal.english)

        # UOU AECC-K-101 additions
        w_khaap = kumaoni.lookup("खाप")
        self.assertIsNotNone(w_khaap)
        self.assertIn("mouth", w_khaap.english)

        w_rees = kumaoni.lookup("रीस")
        self.assertIsNotNone(w_rees)
        self.assertIn("anger", w_rees.english)

        w_hudka = kumaoni.lookup("हुड़का")
        self.assertIsNotNone(w_hudka)
        self.assertIn("drum", w_hudka.english)

        # Newly mined primary source lemmas
        w_talaun = kumaoni.lookup("तलाऊँ")
        self.assertIsNotNone(w_talaun)
        self.assertIn("irrigated", w_talaun.english)

        w_thulma = kumaoni.lookup("थुलमा")
        self.assertIsNotNone(w_thulma)
        self.assertIn("blanket", w_thulma.english)

        w_bhumyal = kumaoni.lookup("भूम्याल")
        self.assertIsNotNone(w_bhumyal)
        self.assertIn("guardian", w_bhumyal.english)


        # Proverbs scale
        provs = kumaoni.proverbs.all()
        self.assertGreaterEqual(len(provs), 80)

        # Riddles scale
        riddles = kumaoni.riddles.all()
        self.assertGreaterEqual(len(riddles), 40)

        # Phrases & idioms scale
        phrases = kumaoni.phrases.all()
        self.assertGreaterEqual(len(phrases), 150)
        idiom = next((p for p in phrases if p.get("kumaoni") == "हात मलन"), None)
        self.assertIsNotNone(idiom)
        self.assertEqual(idiom.get("category"), "idioms")

    def test_cultural_and_surname_words(self):
        # Instruments
        w_damuwa = kumaoni.lookup("दमुवां")
        self.assertIsNotNone(w_damuwa)
        self.assertIn("drum", w_damuwa.english.lower())

        w_masak = kumaoni.lookup("मसकबीन")
        self.assertIsNotNone(w_masak)
        self.assertIn("bagpipe", w_masak.english.lower())

        w_ransingha = kumaoni.lookup("रणसिंगा")
        self.assertIsNotNone(w_ransingha)
        self.assertIn("horn", w_ransingha.english.lower())

        # Marriage
        w_byo = kumaoni.lookup("ब्यो")
        self.assertIsNotNone(w_byo)
        self.assertIn("marriage", w_byo.english.lower())

        w_pithyaan = kumaoni.lookup("पिथ्याँ")
        self.assertIsNotNone(w_pithyaan)
        self.assertIn("mark", w_pithyaan.english.lower())

        w_pichhauda = kumaoni.lookup("रंग्वाली पिछौड़ा")
        self.assertIsNotNone(w_pichhauda)
        self.assertIn("dupatta", w_pichhauda.english.lower())

        # Kinship
        w_kaaka = kumaoni.lookup("काका")
        self.assertIsNotNone(w_kaaka)
        self.assertIn("uncle", w_kaaka.english.lower())

        w_maama = kumaoni.lookup("मामा")
        self.assertIsNotNone(w_maama)
        self.assertIn("uncle", w_maama.english.lower())

        w_gauntyar = kumaoni.lookup("गौंत्यार")
        self.assertIsNotNone(w_gauntyar)
        self.assertIn("villager", w_gauntyar.english.lower())

        # Surnames & Social
        w_bisht = kumaoni.lookup("बिष्ट")
        self.assertIsNotNone(w_bisht)
        self.assertIn("surname", w_bisht.english.lower())

        w_pant = kumaoni.lookup("पंत")
        self.assertIsNotNone(w_pant)
        self.assertIn("surname", w_pant.english.lower())

        w_that = kumaoni.lookup("थात")
        self.assertIsNotNone(w_that)
        self.assertIn("ancestral", w_that.english.lower())


if __name__ == "__main__":
    unittest.main()
