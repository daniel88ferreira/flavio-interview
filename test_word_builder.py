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
        word_pieces = ['pa', 'p', 'al', 'av', 'ra', 'la', 'vr']
        expected = [1,2,3,4]
        self.assertEqual(expected, self.wb.build(word=word, word_pieces=word_pieces))

    def test_word_build_impossible(self):
        word = "palavra"
        word_pieces = ['ba', 't', 'at', 'oz', 'ia']
        expected = []
        self.assertEqual(expected, self.wb.build(word=word, word_pieces=word_pieces))


    def test_word_build_with_missing_pieces(self):
        word = "palavra"
        word_pieces = ['pa', 'la', 'v', 'a']
        self.assertRaises(RuntimeError,
                          lambda: self.wb.build(word=word, word_pieces=word_pieces))

    def test_get_pieces_in_order(self):
        word = "pai"
        word_pieces = ['i', 'pa']
        expected = ['pa', 'i']
        self.assertEqual(expected, self.wb.get_pieces_in_order(word_pieces, word))

    def test_word_pieces_match_word(self):
        word = "pai"
        word_pieces = ['pa', 'i']
        self.assertEqual(True, self.wb.word_pieces_match_word(word_pieces, word))

        word_pieces = ['pato', 'i']
        self.assertEqual(False, self.wb.word_pieces_match_word(word_pieces, word))

    def test_del_item_from_list(self):
        my_list = ['a','b','c']
        my_list_without_b = ['a', 'c']
        self.assertEqual(self.wb.del_item_from_list('b', my_list), my_list_without_b)

    def test_del_piece_from_word(self):
        word = 'batata'
        without_ba = 'tata'
        self.assertEqual(without_ba, self.wb.del_piece_from_word('ba', word))


if __name__ == '__main__':
    unittest.main()
