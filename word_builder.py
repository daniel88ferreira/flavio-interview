

class WordBuilder():
    def build(self, word, word_pieces):
        all_letters_in_word_pieces = ''
        for piece in word_pieces:
            all_letters_in_word_pieces += piece
        if len(all_letters_in_word_pieces) < len(word):
            raise RuntimeError("Not enough letters in word pieces!")

        if len(word_pieces) == 1:
            return [0]
        idx_list = []
        letters = list(word)
        jump = False
        for idx, letter in enumerate(letters):
            if jump == True:
                jump = False
                continue
            try:
                two_letters = letter + letters[idx+1]
                if two_letters in word_pieces:
                    idx_list.append(word_pieces.index(two_letters))
                    jump = True
                elif letter in word_pieces:
                    idx_list.append(word_pieces.index(letter))
            except IndexError:
                if letter in word_pieces:
                    idx_list.append(word_pieces.index(letter))
        return idx_list