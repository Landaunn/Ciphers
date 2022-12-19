alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class Cesar:
    def __init__(self, shift=1):
        self.shift = shift
        self.letter2idx = {char: idx for idx, char in enumerate(alphabet)}
        self.idx2letter = {idx: char for idx, char in enumerate(alphabet)}

        self.shifted_letter2idx = {letter:idx + self.shift for idx, letter in enumerate(alphabet)}
        self.shifted_idx2letter = {idx + self.shift:letter for idx, letter in enumerate(alphabet)}

    def encrypt(self, phrase):
        phrase = phrase.lower()
        encrypted_phrase= []
        for char in phrase:
            if char not in alphabet:
                encrypted_phrase += [char]
            else:
                idx = self.letter2idx[char] + self.shift
                encrypted_phrase += [self.idx2letter[idx % len(alphabet)]]

        return ''.join(encrypted_phrase)

    def decipher(self, phrase):
        phrase = phrase.lower()
        decipher_phrase = []

        for char in phrase:
            if char not in alphabet:
                decipher_phrase += [char]
            else:
                idx = self.letter2idx[char] - self.shift
                idx = idx if idx >= 0 else len(alphabet) + idx
                decipher_phrase += [self.idx2letter[idx % len(alphabet)]]
            
        return ''.join(decipher_phrase)
    