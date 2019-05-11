def isograma(word):
    if not isinstance(word, str):
        return False

    word = word.lower()

    for letra in word:
        if letra.isdigit() or word.count(letra) != 1:
            return False

    return True


if __name__ == '__main__':
    word = input('Digite a palavra: ')
    res = isograma(word)
    if res:
        print('É Isograma')
    else:
        print('Não é Isograma')