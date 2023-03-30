import unittest
from translator import english_to_french, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):
    def test_english(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'),'Hello')






class TestFrenchToEnglish(unittest.TestCase):
    def test_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Hello'),'Bonjour')





unittest.main()
