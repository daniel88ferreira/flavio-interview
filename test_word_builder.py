import unittest
from word_builder import WordBuilder


class TestWordBuilder(unittest.TestCase):
    def setUp(self):
        self.wb = WordBuilder()

    def test_word_build_simple(self):
        word = "pai"
        word_pieces = ['pai']
        expected = [0]
        self.assertEqual(self.wb.build(word=word, word_pieces=word_pieces), expected)

    def test_word_build_short_word(self):
        word = "bola"
        word_pieces = ['ol', 'a', 'b']
        expected = [2,0,1]
        self.assertEqual(self.wb.build(word=word, word_pieces=word_pieces), expected)

    def test_word_build_long(self):
        word = "palavra"
        word_pieces = [ 'la', 'pa', 'v', 'a', 'r']
        expected = [1,0,2,4,3]
        self.assertEqual(self.wb.build(word=word, word_pieces=word_pieces), expected)

    def test_word_build_with_missing_pieces(self):
        word = "palavra"
        word_pieces = ['pa', 'la', 'v', 'a']
        self.assertRaises(RuntimeError("Not enough letters in word pieces!"), self.wb.build(word=word, word_pieces=word_pieces))