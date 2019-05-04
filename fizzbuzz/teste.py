import unittest
from fizzbuzz import fizzBuzz


class FizzBuzz(unittest.TestCase):

    def test_numero_quise(self):
        resultado = fizzBuzz(15)
        self.assertEqual('FizzBuzz', resultado)
        
    def test_numero_zero(self):
        resultado = fizzBuzz(0)
        self.assertEqual('FizzBuzz', resultado)
        
    def test_numero_tres(self):
        resultado = fizzBuzz(3)
        self.assertEqual('Fizz', resultado)
    
    def test_numero_cinco(self):
        resultado = fizzBuzz(5)
        self.assertEqual('Buzz', resultado)
    
    def test_numero_seis(self):
        resultado = fizzBuzz(6)
        self.assertEqual('Fizz', resultado)

    def test_numero_50(self):
        resultado = fizzBuzz(50)
        self.assertEqual('Buzz', resultado)
    
    def test_numero_30(self):
        resultado = fizzBuzz(30)
        self.assertEqual('FizzBuzz', resultado)
    
    def test_numero_7(self):
        resultado = fizzBuzz(7)
        self.assertEqual('7', resultado)