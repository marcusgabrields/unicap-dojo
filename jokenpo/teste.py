import test
import unittest
from jokenpo import jokenpo

class testJokenpo(unittest.TestCase):

    def test_tesoura_vs_papel(self):
        resultado = jokenpo('tesoura', 'papel')
        self.assertEqual('Tesoura Ganha', resultado)
    
    def test_tesoura_vs_pedra(self):
        resultado = jokenpo('tesoura', 'pedra')
        self.assertEqual('Pedra ganha', resultado)

    def teste_tesoura_vs_tesoura(self):
        resultado = jokenpo('tesoura', "tesoura")
        self.assertEqual('Empate', resultado)
    
    def teste_pedra_vs_papel(self):
        resultado = jokenpo('pedra', 'papel')
        self.assertEqual('Papel Ganha', resultado)

    def test_pedra_vs_tesoura(self):
        resultado = jokenpo('pedra', 'tesoura')
        self.assertEqual('Pedra Ganha', resultado)

    def test_pedra_vs_pedra(self):
        resultado = jokenpo('pedra', 'pedra')
        self.assertEqual('Empate', resultado)
    
    def test_papel_vs_pedra(self):
        resultado = jokenpo('papel', 'pedra')
        self.assertEqual('Papel ganha', resultado)
    
    def test_papel_vs_tesoura(self):
        resultado = jokenpo('papel', 'tesoura')
        self.assertEqual('Tesoura ganha', resultado)
    
    def test_papel_vs_papel(self):
        resultado = jokenpo('papel','papel')
        self.assertEqual('Empate', resultado)

    
