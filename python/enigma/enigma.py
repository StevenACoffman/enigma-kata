class Enigma(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #default value
    reflector = alphabet
    #default value
    leftRotor = alphabet


    def encrypt(self, message):
        encrypted_message = message.translate(str.maketrans(self.alphabet, self.leftRotor))
        encrypted_message = encrypted_message.translate(str.maketrans(self.alphabet, self.reflector))
        return encrypted_message.translate(str.maketrans(self.leftRotor, self.alphabet))
