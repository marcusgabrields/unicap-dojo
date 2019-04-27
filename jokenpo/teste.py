import unittest

from jokenpo import jokenpo


class TestJokenpo(unittest.TestCase):
    def test_casos(self):
        casos_teste = [
            ({'input1': 'tesoura', 'input2': 'papel'}, 'Tesoura Ganha'),
            ({'input1': 'papel', 'input2': 'tesoura'}, 'Tesoura Ganha'),
            ({'input1': 'pedra', 'input2': 'tesoura'}, 'Pedra Ganha'),
            ({'input1': 'tesoura', 'input2': 'pedra'}, 'Pedra Ganha'),
            ({'input1': 'pedra', 'input2': 'papel'}, 'Papel Ganha'),
            ({'input1': 'papel', 'input2': 'papel'}, 'Empate'),
            ({'input1': 'pedra', 'input2': 'pedra'}, 'Empate'),
            ({'input1': 'tesoura', 'input2': 'tesoura'}, 'Empate'),
            ({'input1': '', 'input2': ''}, 'Empate')
        ]

        for inputs, output in casos_teste:
            resultado = jokenpo(inputs.get('input1'), inputs.get('input2'))
            self.assertEqual(output, resultado)


if __name__ == '__main__':
    unittest.main()
