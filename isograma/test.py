import unittest

from isograma import isograma


class IsogramaTest(unittest.TestCase):

    def test_string_vazia(self):
        resultado = isograma('')
        self.assertTrue(resultado)

    def test(self):
        resultado = isograma("ABC")
        self.assertTrue(resultado)

    def testD(self):
        resultado = isograma("1")
        self.assertFalse(resultado)

    def test_log_word(self):
        self.assertTrue(isograma('Dermatoglyphics'))

    def test_sensitive_case(self):
        self.assertFalse(isograma('aA'))

    def test_spaces(self):
        self.assertFalse(isograma('  '))

    def test_space(self):
        self.assertTrue(isograma(' '))

    def test_other_type(self):
        self.assertFalse(isograma(1))
