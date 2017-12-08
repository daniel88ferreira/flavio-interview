

class WordBuilder():
    def build(self, word, word_pieces):
        my_word = word
        ## make a backup, because since lists are mutable, python passes them as references
        my_word_pieces = list(word_pieces)

        ## just to count the number of letters in words pieces,
        ## and raise exception is there is not enough letters to build
        ## the word.
        all_letters_in_word_pieces = ''
        for piece in my_word_pieces:
            all_letters_in_word_pieces += piece
        if len(all_letters_in_word_pieces) < len(my_word):
            raise RuntimeError("Not enough letters in word pieces!")

        ## if there is only one piece, return that piece.
        ## It should match the word
        if len(my_word_pieces) == 1:
            return [0]

        ## code that does something is here.
        pieces_in_order = self.get_pieces_in_order(my_word_pieces, my_word)
        idx_in_order = []
        for piece in pieces_in_order:
            idx_in_order.append(word_pieces.index(piece))
        if len(pieces_in_order) == 0:
            print("Impossible match!")
        return idx_in_order

    # recursive function
    def get_pieces_in_order(self, word_pieces, word):
        pieces_in_order = []
        next_piece_candidates = self.find_starting_pieces_candidates(word_pieces, word)
        for next_piece_candidate in next_piece_candidates:
            pieces_in_order = []
            pieces_in_order.append(next_piece_candidate)
            pieces_in_order += self.get_pieces_in_order(self.del_item_from_list(next_piece_candidate, word_pieces),
                                                       self.del_piece_from_word(next_piece_candidate, word))
            if self.word_pieces_match_word(pieces_in_order, word):
                break
        return pieces_in_order

    def find_starting_pieces_candidates(self, word_pieces, word):
        starting_pieces = []
        for piece in word_pieces:
            if word.startswith(piece):
                starting_pieces.append(piece)
        return starting_pieces

    def word_pieces_match_word(self, word_pieces, word):
        word_from_pieces = ''
        for piece in word_pieces:
            word_from_pieces += piece
        return word_from_pieces == word

    def del_piece_from_word(self, piece, word):
        if word.startswith(piece):
            word = word[len(piece):]
        return word

    def del_item_from_list(self, element, pylist):
        pylist_without_element = pylist
        del pylist_without_element[pylist_without_element.index(element)]
        return pylist_without_element
