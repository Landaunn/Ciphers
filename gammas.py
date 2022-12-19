A = 15
B = 17
M = 4096
x = 4003


class Gamma:
    def get_gamma(self, phrase):
        gamma = [(A * x + B) % M] * len(phrase)
        
        return gamma
        
    def encrypt(self, phrase):
        gammas = self.get_gamma(phrase)
        
        return ''.join([chr(ord(char) ^ gamma) for char, gamma in zip(phrase, gammas)])
    
    def decipher(self, phrase):
        return self.encrypt(phrase)
