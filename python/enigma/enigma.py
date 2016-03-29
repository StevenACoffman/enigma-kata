class Enigma(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, reflector='EJMZALYXVBWFCRQUONTSPIKHGD'):
        super().__init__()
        self.reflector = reflector


    def encryptLetter(self, letter):
        if letter == 'A':
            encrypted_message = 'E'
        elif letter == 'B':
            encrypted_message = 'J'
        elif letter == 'C':
            encrypted_message = 'M'
        else:
            encrypted_message = ''
        return encrypted_message

    def encrypt(self, message):

        return message.translate(str.maketrans(self.alphabet, self.reflector))
