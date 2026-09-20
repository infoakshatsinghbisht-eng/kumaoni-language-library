import unittest
import kumaoni


class TestTranslator(unittest.TestCase):
    def test_english_translation(self):
        res1 = kumaoni.translate("How are you?", source="en")
        self.assertIn("कस छू तुम?", str(res1))
        self.assertIsNotNone(res1.romanized)

        res2 = kumaoni.translate("What is your name?", source="en")
        self.assertIn("तुमार नाम क्या छ?", str(res2))

        res3 = kumaoni.translate("Where is the water?", source="en")
        self.assertIn("पाणि कहाँ छ?", str(res3))

    def test_english_words_translation(self):
        # Single English words
        self.assertEqual(str(kumaoni.translate("mother")), "ईजा")
        self.assertEqual(str(kumaoni.translate("father")), "बाबु")
        self.assertEqual(str(kumaoni.translate("water")), "पाणि")
        self.assertEqual(str(kumaoni.translate("sugar")), "चीनी")
        self.assertEqual(str(kumaoni.translate("tree")), "रुख")
        self.assertEqual(str(kumaoni.translate("sun")), "घाम")
        self.assertEqual(str(kumaoni.translate("moon")), "ज्यून्या")
        self.assertEqual(str(kumaoni.translate("love")), "माया")
        self.assertEqual(str(kumaoni.translate("banana")), "केला")
        self.assertEqual(str(kumaoni.translate("elephant")), "हाथी")
        self.assertEqual(str(kumaoni.translate("help")), "मदद")
        self.assertEqual(str(kumaoni.translate("because")), "किलैकि")

    def test_english_synonyms_and_colloquials(self):
        # Mother synonyms
        for m in ("mom", "mum", "mommy", "mummy", "mama", "maa", "ma"):
            self.assertEqual(str(kumaoni.translate(m)), "ईजा", f"Failed for {m}")
            self.assertEqual(kumaoni.lookup(m).kumaoni, "ईजा", f"Lookup failed for {m}")

        # Father synonyms
        for f in ("dad", "daddy", "papa", "pop", "pa", "pitaji"):
            self.assertEqual(str(kumaoni.translate(f)), "बाबु", f"Failed for {f}")
            self.assertEqual(kumaoni.lookup(f).kumaoni, "बाबु", f"Lookup failed for {f}")

        # Grandparent synonyms
        for gp in ("grandpa", "granddad", "dada", "nana"):
            self.assertEqual(str(kumaoni.translate(gp)), "बूबू", f"Failed for {gp}")
            self.assertEqual(kumaoni.lookup(gp).kumaoni, "बूबू", f"Lookup failed for {gp}")

        for gm in ("grandma", "granny", "dadi", "nani"):
            self.assertEqual(str(kumaoni.translate(gm)), "आमा", f"Failed for {gm}")
            self.assertEqual(kumaoni.lookup(gm).kumaoni, "आमा", f"Lookup failed for {gm}")

        # Sibling synonyms
        self.assertEqual(str(kumaoni.translate("bro")), "दाज्यू")
        self.assertEqual(str(kumaoni.translate("sis")), "दीदी")

        # Children & youth synonyms
        for c in ("kid", "child", "baby", "infant"):
            self.assertEqual(str(kumaoni.translate(c)), "नातिन", f"Failed for {c}")
        for cs in ("kids", "children"):
            self.assertEqual(str(kumaoni.translate(cs)), "नान्तिन", f"Failed for {cs}")

    def test_english_sentences_grammar(self):
        # Progressive aspect
        res_prog = kumaoni.translate("She is eating food")
        self.assertIn("खाण लागूँ", str(res_prog))

        # Desiderative / Needs
        res_want = kumaoni.translate("I want water")
        self.assertIn("मैंकणी पाणि चाही", str(res_want))

        # Prohibitive
        res_proh = kumaoni.translate("Do not go")
        self.assertIn("झनि जाया", str(res_proh))

        # Equative SVO -> SOV
        res_house = kumaoni.translate("This is my house")
        self.assertIn("यो मेरो घर छ", str(res_house))

        # Imperative
        res_give = kumaoni.translate("Give me water")
        self.assertIn("मैंकणी पाणि दिया", str(res_give))

    def test_hindi_translation(self):
        res1 = kumaoni.translate("आप कैसे हैं?", source="hi")
        self.assertIn("कस छू तुम?", str(res1))

        res2 = kumaoni.translate("मैं ठीक हूँ।", source="hi")
        self.assertIn("मैं ठीक छूँ।", str(res2))

    def test_uttarakhandi_vocabulary(self):
        # Kinship & Relations
        self.assertEqual(str(kumaoni.translate("grandfather")), "बूबू")
        self.assertEqual(str(kumaoni.translate("paternal grandfather")), "बरबाज्यू")
        res_yb = str(kumaoni.translate("younger brother"))
        self.assertTrue(res_yb in ("भै", "भुला"))
        res_dil = str(kumaoni.translate("daughter-in-law"))
        self.assertTrue(res_dil in ("बुआरी", "ब्वारी", "ब्वारि"))
        res_sil = str(kumaoni.translate("son-in-law"))
        self.assertTrue(res_sil in ("ज्वै", "जवाइन"))
        res_aunt = str(kumaoni.translate("aunt"))
        self.assertTrue(res_aunt in ("काकी", "काखी"))
        res_fr = str(kumaoni.translate("friend"))
        self.assertTrue(res_fr in ("दगड़्या", "दगड़ि", "दगड़ी", "संगी"))
        res_hus = str(kumaoni.translate("husband"))
        self.assertTrue(res_hus in ("सैं", "घरवाला"))
        res_wife = str(kumaoni.translate("wife"))
        self.assertTrue(res_wife in ("घरवाली", "स्याणी", "सयाणी", "ब्याति"))

        # Nature, Directions & Objects
        res_here = str(kumaoni.translate("here"))
        self.assertTrue(res_here in ("एतला", "एथर", "याँ", "येथर"))
        res_there = str(kumaoni.translate("there"))
        self.assertTrue(res_there in ("उतला", "उथर", "त्याँ", "वेथर"))
        res_place = str(kumaoni.translate("place"))
        self.assertTrue(res_place in ("थान", "ठाऊँ", "जागा"))
        self.assertEqual(str(kumaoni.translate("flower")), "फूल")
        self.assertEqual(str(kumaoni.translate("leaf")), "पात")
        self.assertEqual(str(kumaoni.translate("root")), "जड़")
        self.assertEqual(str(kumaoni.translate("fire")), "आग")
        res_bird = str(kumaoni.translate("bird"))
        self.assertTrue(res_bird in ("चिल्या", "चड़ि", "चड़ी"))
        self.assertEqual(str(kumaoni.translate("shoes")), "जूतो")
        self.assertEqual(str(kumaoni.translate("door")), "कवाड़")
        self.assertEqual(str(kumaoni.translate("clothes")), "गाभा")
        self.assertEqual(str(kumaoni.translate("life")), "जिंदगी")
        self.assertEqual(str(kumaoni.translate("death")), "मरण")
        self.assertEqual(str(kumaoni.translate("darkness")), "अँधार")
        self.assertEqual(str(kumaoni.translate("light")), "उज्याव")
        self.assertEqual(str(kumaoni.translate("day")), "दिन")
        self.assertEqual(str(kumaoni.translate("fast")), "झटपट")
        res_lw = str(kumaoni.translate("lightweight"))
        self.assertTrue(res_lw in ("हलो", "हलुक"))
        self.assertEqual(str(kumaoni.translate("hungry")), "भूखो")
        self.assertEqual(str(kumaoni.translate("thirsty")), "तिसासो")
        self.assertEqual(str(kumaoni.translate("doctor")), "डाकदर")
        self.assertEqual(str(kumaoni.translate("teacher")), "मास्साब")
        res_boy = str(kumaoni.translate("boy"))
        self.assertTrue(res_boy in ("च्याल", "चेला", "चेलो"))

    def test_uttarakhandi_conversational_phrases(self):
        # Greetings & Polite expressions
        res_meet = str(kumaoni.translate("Nice to meet you"))
        self.assertTrue("तुज भेटक बढ़िया लागो।" in res_meet or "तुमकणी मिलिबेर" in res_meet)
        res_see = str(kumaoni.translate("See you again"))
        self.assertTrue("फिर मिलुला" in res_see or "फिर मिलूँला" in res_see)
        self.assertIn("धन्यवाद!", str(kumaoni.translate("Thank you very much!")))

        # Navigation & Queries
        self.assertIn("यो ठाऊँ कहाँ", str(kumaoni.translate("Where is this place?")))
        self.assertIn("तुमार घर कहाँ छ?", str(kumaoni.translate("Where is your house?")))
        res_cost = str(kumaoni.translate("How much does this cost?"))
        self.assertTrue("कतुक" in res_cost and "छ" in res_cost)
        self.assertIn("के तुम कुमाऊँनी बोलछा?", str(kumaoni.translate("Do you speak Kumaoni?")))
        self.assertIn("मैंकणी नी पत्त।", str(kumaoni.translate("I do not know.")))
        self.assertIn("तुमल क्या खायो?", str(kumaoni.translate("What did you eat?")))

        # Commands & Needs
        res_come = str(kumaoni.translate("Come here."))
        self.assertTrue("एथर आ" in res_come)
        res_go = str(kumaoni.translate("Go there."))
        self.assertTrue("उथर जा" in res_go)
        res_hun = str(kumaoni.translate("I am hungry."))
        self.assertTrue("भूख" in res_hun)
        res_thi = str(kumaoni.translate("I am thirsty."))
        self.assertTrue("तीस" in res_thi or "प्यासी" in res_thi)

        # Wishes & Emotions
        res_love = str(kumaoni.translate("I love you"))
        self.assertTrue("माया" in res_love or "प्रेम" in res_love or "प्यार" in res_love)
        res_bday = str(kumaoni.translate("Happy birthday!"))
        self.assertTrue("जन्मदिन" in res_bday or "जनमदिन" in res_bday)
        self.assertIn("दीपावली", str(kumaoni.translate("Happy Diwali!")))


if __name__ == "__main__":
    unittest.main()
