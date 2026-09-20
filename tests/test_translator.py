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

    def test_hindi_translation(self):
        res1 = kumaoni.translate("आप कैसे हैं?", source="hi")
        self.assertIn("कस छू तुम?", str(res1))

        res2 = kumaoni.translate("मैं ठीक हूँ।", source="hi")
        self.assertIn("मैं ठीक छूँ।", str(res2))

    def test_translation_result_object(self):
        res = kumaoni.translate("Good morning")
        self.assertEqual(res.target_lang, "kmy")
        self.assertGreater(res.confidence, 0.5)
        self.assertIn("शुभ बिहान", str(res))


if __name__ == "__main__":
    unittest.main()
