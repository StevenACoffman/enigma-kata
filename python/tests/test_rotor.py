from unittest import TestCase
from unittest.mock import patch

from ..enigma.rotor import *


# Up to you if you want to write these tests
class SingleLetterRotorTestCase(TestCase):
    def setUp(self):
        self.rotor = Rotor()

    def test_enigma_encrypts_blank_as_blank(self):
        self.assertEqual('', self.rotor.forward_encrypt(''))


class SimpleMessageCipherTestCase(TestCase):
    def setUp(self):
        self.rotor = Rotor()

    def test_rotor_encrypts_a_as_a(self):
        self.assertEqual('B', self.rotor.forward_encrypt('A'))