import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_english_to_french(self):
        # Test for null input
        self.assertIsNone(english_to_french(None))

        # Test translation of 'Hello'
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english(self):
        # Test for null input
        self.assertIsNone(french_to_english(None))

        # Test translation of 'Bonjour'
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')


if __name__ == '__main__':
    unittest.main()
