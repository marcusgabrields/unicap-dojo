def jokenpo(x, y):

    jogada = (x, y)

    if 'pedra' in jogada and 'tesoura' in jogada:
        return 'Pedra Ganha'
    
    if 'tesoura' in jogada and 'papel' in jogada:
        return 'Tesoura Ganha'
    
    if 'papel' in jogada and 'pedra' in jogada:
        return 'Papel Ganha'
    
    return 'Empate'


if __name__ == '__main__':
    jogador1 = input('1ª Jogada: ')
    jogador2 = input('2ª jogada: ')

    print(jokenpo(jogador1, jogador2))
