import unittest
import kumaoni


class TestCulture(unittest.TestCase):
    def test_festivals(self):
        harela = kumaoni.festivals.get("harela")
        self.assertIsNotNone(harela)
        self.assertEqual(harela.name_kumaoni, "हरेला")
        self.assertTrue(len(harela.rituals) > 0)

        all_fests = kumaoni.festivals.list()
        self.assertGreater(len(all_fests), 3)

    def test_calendar_and_seasons(self):
        months = kumaoni.get_months()
        self.assertEqual(len(months), 12)
        self.assertEqual(months[0]["kumaoni"], "चैत")

        seasons = kumaoni.get_seasons()
        self.assertIn("grishma", seasons)
        self.assertEqual(seasons["grishma"]["name_kmy"], "रूड़ि")

    def test_proverbs_and_riddles(self):
        proverb = kumaoni.proverbs.random()
        self.assertIn("kumaoni", proverb)
        self.assertIn("figurative_meaning", proverb)
        all_proverbs = kumaoni.proverbs.all()
        self.assertGreaterEqual(len(all_proverbs), 10)

        riddle = kumaoni.riddles.random()
        self.assertIn("riddle", riddle)
        self.assertIn("answer_kumaoni", riddle)
        all_riddles = kumaoni.riddles.all()
        self.assertGreaterEqual(len(all_riddles), 8)

    def test_literature(self):
        epics = kumaoni.literature.epics()
        self.assertGreaterEqual(len(epics), 6)
        
        malu = kumaoni.literature.get_epic("malushahi")
        self.assertIsNotNone(malu)
        self.assertIn("राजुला", malu.title_kumaoni)

        jiya = kumaoni.literature.get_epic("jiya_rani")
        self.assertIsNotNone(jiya)
        self.assertIn("जिया राँणि", jiya.title_kumaoni)

        haru = kumaoni.literature.get_epic("haru_singh_heet")
        self.assertIsNotNone(haru)
        self.assertIn("हीत", haru.title_kumaoni)

        authors = kumaoni.literature.authors()
        self.assertGreaterEqual(len(authors), 10)
        
        gumani = kumaoni.literature.get_author("gumani_pant")
        self.assertIsNotNone(gumani)
        self.assertIn("गुमानी", gumani.name_kumaoni)

        kp = kumaoni.literature.get_author("krishna_pandey")
        self.assertIsNotNone(kp)
        self.assertIn("कृष्ण", kp.name_kumaoni)
        self.assertIn("Kalyug Varnan", kp.famous_works)

        upreti = kumaoni.literature.get_author("ganga_datt_upreti")
        self.assertIsNotNone(upreti)
        self.assertIn("उप्रेती", upreti.name_kumaoni)

        tp = kumaoni.literature.get_author("trilochan_pandey")
        self.assertIsNotNone(tp)
        self.assertIn("त्रिलोचन", tp.name_kumaoni)

        bdp = kumaoni.literature.get_author("badri_datt_pande")
        self.assertIsNotNone(bdp)
        self.assertIn("बद्री दत्त", bdp.name_kumaoni)
        self.assertIn("Kumaun ka Itihas (1937)", bdp.famous_works)

        gj = kumaoni.literature.get_author("gunanand_juyal")
        self.assertIsNotNone(gj)
        self.assertIn("गुणानन्द", gj.name_kumaoni)

        girda = kumaoni.literature.get_author("girda")
        self.assertIsNotNone(girda)
        self.assertIn("गिर्दा", girda.name_kumaoni)

        rana = kumaoni.literature.get_author("heera_singh_rana")
        self.assertIsNotNone(rana)
        self.assertIn("हीरा सिंह", rana.name_kumaoni)

        # Test new poems
        poems = kumaoni.literature.poems()
        self.assertGreaterEqual(len(poems), 6)
        kalyug_poem = next((p for p in poems if p.id == "kalyug_varnan"), None)
        self.assertIsNotNone(kalyug_poem)
        self.assertIn("कलयुग", kalyug_poem.title_kumaoni)

        ghughuti = next((p for p in poems if p.id == "ghughuti_basuti"), None)
        self.assertIsNotNone(ghughuti)
        self.assertIn("घुघूती", ghughuti.title_kumaoni)


if __name__ == "__main__":
    unittest.main()



