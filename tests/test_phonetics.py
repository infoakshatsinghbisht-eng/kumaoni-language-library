import unittest
import kumaoni
from kumaoni.constants import Script


class TestPhonetics(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(kumaoni.normalize("कुमाँउनी"), "कुमाऊँनी")
        self.assertEqual(kumaoni.normalize("पैलाग़"), "पैलाग")

    def test_detect_script(self):
        self.assertEqual(kumaoni.detect_script("कुमाऊँनी"), Script.DEVANAGARI)
        self.assertEqual(kumaoni.detect_script("Kumaoni"), Script.LATIN)

    def test_transliteration(self):
        self.assertEqual(kumaoni.transliterate("dajyu", to_script="devanagari"), "दाज्यू")
        self.assertEqual(kumaoni.transliterate("ija", to_script="devanagari"), "ईजा")
        self.assertEqual(kumaoni.transliterate("pailag", to_script="devanagari"), "पैलाग")
        
        # Devanagari to Latin
        dev = "पैलाग"
        lat = kumaoni.transliterate(dev, to_script="latin").lower()
        self.assertTrue("pailaag" in lat or "pailag" in lat or "palag" in lat)

    def test_tokenization(self):
        tokens = kumaoni.tokenize("कस छू तुम?")
        self.assertIn("कस", tokens)
        self.assertIn("तुम", tokens)
        self.assertIn("?", tokens)


if __name__ == "__main__":
    unittest.main()
