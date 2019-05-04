def fizzBuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'

    if numero % 3 == 0:
        return 'Fizz'

    if numero % 5 == 0:
        return 'Buzz'

    return str(numero)


if __name__ == '__main__':
    tam = int(input('Digite um valor: '))

    lista = range(0, tam + 1)

    for numero in lista:
        print(fizzBuzz(numero))