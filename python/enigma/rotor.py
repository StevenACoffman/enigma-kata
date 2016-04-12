class Rotor(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translation = alphabet
    rotates = False
    rotations = 0

    def __init__(self, translation=alphabet):
        self.translation = translation

    def rotate(self, rotations):
        if self.rotates:
            self.rotations += rotations
            self.translation = self.translation[-(rotations % 26):] + self.translation[:-(rotations % 26)]

    def forward_encrypt(self, message):
        return message.translate(str.maketrans(self.alphabet, self.translation))

    def backward_encrypt(self, message):
        return message.translate(str.maketrans(self.translation, self.alphabet))