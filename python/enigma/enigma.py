class Enigma(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, reflector='EJMZALYXVBWFCRQUONTSPIKHGD'):
        super().__init__()
        self.reflector = reflector


    def encrypt(self, message):

        return message.translate(str.maketrans(self.alphabet, self.reflector))
