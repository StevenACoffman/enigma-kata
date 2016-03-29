class Enigma(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # default value
    reflector = 'EJMZALYXVBWFCRQUONTSPIKHGD'
    # default value
    leftRotor = alphabet
    # default value
    centerRotor = alphabet
    #default value
    rightRotor = alphabet

    def encrypt(self, message):
        encrypted_message = message
        encrypted_message = encrypted_message.translate(str.maketrans(self.alphabet, self.rightRotor))
        encrypted_message = encrypted_message.translate(str.maketrans(self.alphabet, self.centerRotor))
        # print('center rotor:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(self.alphabet, self.leftRotor))
        # print('leftRotor:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(self.alphabet, self.reflector))
        # print('reflector:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(self.leftRotor, self.alphabet))
        # print('leftRotorBackwards:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(self.centerRotor, self.alphabet))
        # print('centerRotorBackwards:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(self.rightRotor, self.alphabet))
        return encrypted_message
