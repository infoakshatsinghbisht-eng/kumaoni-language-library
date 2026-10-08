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

        # Trees & Plants
        w_banjh = kumaoni.lookup("बाँझ")
        self.assertIsNotNone(w_banjh)
        w_buransh = kumaoni.lookup("बुराँश")
        self.assertIsNotNone(w_buransh)
        w_brahmakamal = kumaoni.lookup("ब्रह्मकमल")
        self.assertIsNotNone(w_brahmakamal)
        w_panya = kumaoni.lookup("पैंया")
        self.assertIsNotNone(w_panya)
        w_ringal = kumaoni.lookup("रिंगाल")
        self.assertIsNotNone(w_ringal)
        w_bheemal = kumaoni.lookup("भीमल")
        self.assertIsNotNone(w_bheemal)
        w_utees = kumaoni.lookup("उतीस")
        self.assertIsNotNone(w_utees)
        w_semal = kumaoni.lookup("सेमल")
        self.assertIsNotNone(w_semal)
        w_bhaang = kumaoni.lookup("भांग")
        self.assertIsNotNone(w_bhaang)
        w_sisoon = kumaoni.lookup("सिसूण")
        self.assertIsNotNone(w_sisoon)
        w_gaderi = kumaoni.lookup("गड़ेरी")
        self.assertIsNotNone(w_gaderi)

        # Temple & Ritual items
        w_hawankund = kumaoni.lookup("हवनकुंड")
        self.assertIsNotNone(w_hawankund)
        w_samidha = kumaoni.lookup("समिधा")
        self.assertIsNotNone(w_samidha)
        w_panchapatra = kumaoni.lookup("पंचपात्र")
        self.assertIsNotNone(w_panchapatra)
        w_ghant = kumaoni.lookup("घंट")
        self.assertIsNotNone(w_ghant)
        w_trishul = kumaoni.lookup("त्रिशूल")
        self.assertIsNotNone(w_trishul)
        w_paati = kumaoni.lookup("पाती")
        self.assertIsNotNone(w_paati)
        w_rot = kumaoni.lookup("रोट")
        self.assertIsNotNone(w_rot)
        w_dhooni = kumaoni.lookup("धूणी")
        self.assertIsNotNone(w_dhooni)
        w_deewa = kumaoni.lookup("दीवा")
        self.assertIsNotNone(w_deewa)
        w_baati = kumaoni.lookup("बाती")
        self.assertIsNotNone(w_baati)
        w_kapoor = kumaoni.lookup("कपूर")
        self.assertIsNotNone(w_kapoor)
        w_pattal = kumaoni.lookup("पत्तल")
        self.assertIsNotNone(w_pattal)
        w_jantar = kumaoni.lookup("जंतर")
        self.assertIsNotNone(w_jantar)
        w_nath = kumaoni.lookup("नथ")
        self.assertIsNotNone(w_nath)

        # School & Education
        w_school = kumaoni.lookup("ईस्कूल")
        self.assertIsNotNone(w_school)
        self.assertEqual(w_school.category, "education")
        w_master = kumaoni.lookup("मास्साब")
        self.assertIsNotNone(w_master)
        w_pathri = kumaoni.lookup("पाथरी")
        self.assertIsNotNone(w_pathri)
        w_batti = kumaoni.lookup("बत्ती")
        self.assertIsNotNone(w_batti)
        w_maswani = kumaoni.lookup("मसवाणी")
        self.assertIsNotNone(w_maswani)
        w_banchan = kumaoni.lookup("बांचण")
        self.assertIsNotNone(w_banchan)

        # Jobs, Government & Office
        w_sarkari = kumaoni.lookup("सरकारी नौकरी")
        self.assertIsNotNone(w_sarkari)
        w_hakim = kumaoni.lookup("हाकिम")
        self.assertIsNotNone(w_hakim)
        w_patwari = kumaoni.lookup("पटवारी")
        self.assertIsNotNone(w_patwari)
        w_talab = kumaoni.lookup("तलब")
        self.assertIsNotNone(w_talab)
        w_kachhari = kumaoni.lookup("कचहरी")
        self.assertIsNotNone(w_kachhari)
        w_arzi = kumaoni.lookup("अर्जी")
        self.assertIsNotNone(w_arzi)
        w_misil = kumaoni.lookup("मिसिल")
        self.assertIsNotNone(w_misil)
        w_dastkhat = kumaoni.lookup("दस्तखत")
        self.assertIsNotNone(w_dastkhat)

        # Business & Trade
        w_byapar = kumaoni.lookup("ब्यापार")
        self.assertIsNotNone(w_byapar)
        w_mahajan = kumaoni.lookup("महाजन")
        self.assertIsNotNone(w_mahajan)
        w_taraju = kumaoni.lookup("तराजू")
        self.assertIsNotNone(w_taraju)

        # Crime, Corruption & Scams
        w_ghoos = kumaoni.lookup("घूस")
        self.assertIsNotNone(w_ghoos)
        w_ghotala = kumaoni.lookup("घोटाला")
        self.assertIsNotNone(w_ghotala)
        w_thag = kumaoni.lookup("ठग")
        self.assertIsNotNone(w_thag)
        w_chori = kumaoni.lookup("चोरी")
        self.assertIsNotNone(w_chori)
        w_daka = kumaoni.lookup("डाका")
        self.assertIsNotNone(w_daka)
        w_hathkadi = kumaoni.lookup("हथकड़ी")
        self.assertIsNotNone(w_hathkadi)

        # Home things, Utensils & Crockery
        w_bhaand = kumaoni.lookup("भाण्ड")
        self.assertIsNotNone(w_bhaand)
        w_tambi = kumaoni.lookup("ताँबी")
        self.assertIsNotNone(w_tambi)
        w_batki = kumaoni.lookup("बटकी")
        self.assertIsNotNone(w_batki)
        w_chimto = kumaoni.lookup("चिमटो")
        self.assertIsNotNone(w_chimto)
        w_theki = kumaoni.lookup("ठेकी")
        self.assertIsNotNone(w_theki)
        w_sil = kumaoni.lookup("सिल-लोटा")
        self.assertIsNotNone(w_sil)
        w_doka = kumaoni.lookup("डोका")
        self.assertIsNotNone(w_doka)
        w_chulho = kumaoni.lookup("चुलहो")
        self.assertIsNotNone(w_chulho)
        w_sandook = kumaoni.lookup("सन्दूक")
        self.assertIsNotNone(w_sandook)

        # Children, Infancy, Movements & Rituals
        w_naantin = kumaoni.lookup("नान्तिन")
        self.assertIsNotNone(w_naantin)
        w_doodhpito = kumaoni.lookup("दूधपितो")
        self.assertIsNotNone(w_doodhpito)
        w_gathuli = kumaoni.lookup("गाथुली सरण")
        self.assertIsNotNone(w_gathuli)
        w_ladbad = kumaoni.lookup("लडबड हिटण")
        self.assertIsNotNone(w_ladbad)
        w_tut = kumaoni.lookup("तुत-तुत बोलण")
        self.assertIsNotNone(w_tut)
        w_kolyon = kumaoni.lookup("कोल्यों बैठण")
        self.assertIsNotNone(w_kolyon)
        w_pasni = kumaoni.lookup("पास्नी")
        self.assertIsNotNone(w_pasni)
        w_jyoonr = kumaoni.lookup("ज्यूँड़ कापण")
        self.assertIsNotNone(w_jyoonr)
        w_najar = kumaoni.lookup("नजर उतारण")
        self.assertIsNotNone(w_najar)
        w_ghughuti = kumaoni.lookup("घूघूती बासुती")
        self.assertIsNotNone(w_ghughuti)


if __name__ == "__main__":
    unittest.main()
