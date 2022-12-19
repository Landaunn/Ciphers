alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class Permutation:
    def __init__(self, permute=alphabet):
        self.permute_alphabet = permute
        self.letter2sub = {char: sub for sub, char in zip(alphabet, self.permute_alphabet)}
        self.sub2letter = {sub: char for sub, char in zip(alphabet, self.permute_alphabet)}

    def encrypt(self, phrase):
        phrase = phrase.lower()
        encrypted_phrase= []
        
        for char in phrase:
            if char not in self.letter2sub.keys():
                encrypted_phrase += [char]
            else:
                encrypted_phrase += [self.letter2sub[char]]
        
        return ''.join(encrypted_phrase)

    def decipher(self, phrase):
        phrase = phrase.lower()
        decipher_phrase= []
        
        for char in phrase:
            if char not in self.sub2letter.keys():
                decipher_phrase += [char]
            else:
                decipher_phrase += [self.sub2letter[char]]
        
        return ''.join(decipher_phrase)
