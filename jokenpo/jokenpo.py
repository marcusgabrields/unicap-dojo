jogador1 = input('1ª Jogada: ')
jogador2 = input('2ª jogada: ')

def jokenpo(x, y):

    if x == 'tesoura' and y == 'papel':
        return 'Tesoura Ganha'

    elif x == 'papel' and y == 'pedra':
        return "Papel ganha"

    elif x == 'pedra' and y == 'tesoura':
        return "Pedra Ganha"

    elif x == 'pedra' and y == 'papel':
        return "Papel Ganha"

    elif x == 'tesoura' and y == 'pedra':
        return 'Pedra ganha'
    
    elif x == 'papel' and y == 'tesoura':
        return 'Tesoura ganha'
    
    else:
        return 'Empate'


print(jokenpo(jogador1, jogador2))