import unittest
from translator import english_to_french, french_to_english

class TestTeanslator(unittest.TestCase):

    def test_frenchToEnglish(self):
        self.assertNotEqual(french_to_english("None"), " ")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_EnglishToFrench(self):
        self.assertNotEqual(english_to_french("None"), " ")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

unittest.main()
