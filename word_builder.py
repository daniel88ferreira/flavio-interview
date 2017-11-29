

class WordBuilder():
    def build(self, word, word_pieces):


        ## just to count the number of letters in words pieces,
        ## and raise exception is there is not enough letter to build
        ## the word.
        all_letters_in_word_pieces = ''
        for piece in word_pieces:
            all_letters_in_word_pieces += piece
        if len(all_letters_in_word_pieces) < len(word):
            raise RuntimeError("Not enough letters in word pieces!")


        ## if there is only one piece, return that piece.
        ## It should match the word
        if len(word_pieces) == 1:
            return [0]


        ## code that does something is here,
        ## only works with pieces of one or two letters
        idx_list = []
        letters = list(word)
        skip_next_letter = False

        for idx, letter in enumerate(letters):
            if skip_next_letter == True:
                skip_next_letter = False
                continue
            try:
                two_letters = letter + letters[idx+1]
                if two_letters in word_pieces:
                    idx_list.append(word_pieces.index(two_letters))
                    skip_next_letter = True
                elif letter in word_pieces:
                    idx_list.append(word_pieces.index(letter))
            except IndexError:
                if letter in word_pieces:
                    idx_list.append(word_pieces.index(letter))
        return idx_list