def jokenpo(x, y):

    if x == 'tesoura' and y == 'papel':
        return 'Tesoura Ganha'

    elif x == 'papel' and y == 'pedra':
        return "Papel Ganha"

    elif x == 'pedra' and y == 'tesoura':
        return "Pedra Ganha"

    elif x == 'pedra' and y == 'papel':
        return "Papel Ganha"

    elif x == 'tesoura' and y == 'pedra':
        return 'Pedra Ganha'

    elif x == 'papel' and y == 'tesoura':
        return 'Tesoura Ganha'

    else:
        return 'Empate'


if __name__ == '__main__':
    jogador1 = input('1ª Jogada: ')
    jogador2 = input('2ª jogada: ')

    print(jokenpo(jogador1, jogador2))
