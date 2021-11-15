#!/usr/bin/env python
"""
Unit tests for pangram.py
"""
import unittest

import pangram


class TestIt(unittest.TestCase):

    # def test_contains_pangram_false(self):
    #     text = 'abc'
    #     self.assertFalse(pangram.contains_pangram(text))

    def test_contains_pangram_true(self):
        text = (
            "About 1,300,000,000 results (0.47 seconds) Search ResultsThe "
            "quick brown fox jumps over the lazy dog - "
            "Wikipedia ...en.wikipedia.org/wiki/The_quick_brown_fox_jumps_"
            "over_the_lazy_dog The quick brown fox jumps over the lazy "
            "dog is an English-language pangram—a phrase that contains "
            "all of the letters of the alphabet. It is used to show font"
        )
        self.assertTrue(pangram.contains_pangram(text))

    def test_find_pangram(self):
        text = (
            " - Wikipedia The quick brown fox jumps over the lazy dog is "
            "an English-language pangram—a phrase that contains all of "
            "the letters of the alphabet. It is used to show font"
        )

        found, index = pangram.find_pangram(text)

        self.assertEqual(found, "quick brown fox jumps over the lazy dog")

    def test_find_pangram_two(self):
        text = (
            "The best known pangram: The quick brown fox jumps over the "
            "lazy dog. Followed by a perfect pangram: Cwm fjord bank "
            "glyphs vext quiz"
        )

        found, index = pangram.find_pangram(text)

        self.assertEqual(found, "cwm fjord bank glyphs vext quiz")


if __name__ == "__main__":
    unittest.main()

# End of file
