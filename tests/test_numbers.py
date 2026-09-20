import unittest
import kumaoni


class TestNumbers(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(kumaoni.num_to_words(0), "शून्य")
        self.assertEqual(kumaoni.num_to_words(1), "एक")
        self.assertEqual(kumaoni.num_to_words(2), "द्वी")
        self.assertEqual(kumaoni.num_to_words(10), "दस")
        self.assertEqual(kumaoni.num_to_words(42), "बयालीस")

    def test_romanized_numbers(self):
        self.assertEqual(kumaoni.num_to_words(2, script="latin"), "dwi")
        self.assertEqual(kumaoni.num_to_words(42, script="latin"), "bayalees")

    def test_large_numbers(self):
        words = kumaoni.num_to_words(108)
        self.assertEqual(words, "एक सौ आठ")

    def test_devanagari_numerals(self):
        self.assertEqual(kumaoni.to_devanagari_numerals(1234), "१२३४")
        self.assertEqual(kumaoni.from_devanagari_numerals("१२३४"), 1234)

    def test_ordinals_and_fractions(self):
        self.assertEqual(kumaoni.ordinal(1), "पैलो")
        self.assertEqual(kumaoni.ordinal(2), "दुसर")
        self.assertEqual(kumaoni.fraction(1, 2), "आधो")
        self.assertEqual(kumaoni.fraction(1, 4), "पाव")

    def test_words_to_num(self):
        self.assertEqual(kumaoni.words_to_num("बयालीस"), 42)
        self.assertEqual(kumaoni.words_to_num("एक सौ आठ"), 108)


if __name__ == "__main__":
    unittest.main()
