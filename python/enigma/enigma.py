from .rotor import Rotor


class Enigma(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # default value
    reflector = 'EJMZALYXVBWFCRQUONTSPIKHGD'
    # default value
    left_rotor = Rotor(alphabet)
    # default value
    center_rotor = Rotor(alphabet)
    # default value
    right_rotor = Rotor(alphabet)

    def set_right_rotor(self, translation):
        self.right_rotor.translation = translation

    def set_center_rotor(self, translation):
        self.center_rotor.translation = translation

    def set_left_rotor(self, translation):
        self.left_rotor.translation = translation

    def encrypt(self, message):
        encrypted_message = message
        encrypted_message = self.right_rotor.forward_encrypt(encrypted_message)
        encrypted_message = self.center_rotor.forward_encrypt(encrypted_message)
        # print('center rotor:' + encrypted_message)
        encrypted_message =self.left_rotor.forward_encrypt(encrypted_message)
        # print('left_rotor:' + encrypted_message)
        encrypted_message = encrypted_message.translate(str.maketrans(
            self.alphabet, self.reflector))
        # print('reflector:' + encrypted_message)

        encrypted_message = self.right_rotor.backward_encrypt(encrypted_message)
        # print('left_rotorBackwards:' + encrypted_message)
        encrypted_message = self.center_rotor.backward_encrypt(encrypted_message)
        # print('center_rotorBackwards:' + encrypted_message)
        encrypted_message = self.left_rotor.backward_encrypt(encrypted_message)
        return encrypted_message
