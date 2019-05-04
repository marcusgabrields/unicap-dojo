tam = int(input('Digite o tamanho da lista'))

lista = range(0, tam)

def fizzBuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'

    if numero % 3 == 0:
        return 'Fizz'

    if numero % 5 == 0:
        return 'Buzz'

    return str(numero)

for numero in lista:
    print(fizzBuzz(numero))