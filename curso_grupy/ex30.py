'''Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o resto de 
uma divisão. Por exemplo: 3 % 2 = 1 e 4 % 2 = 0'''


numero = int(input('digite um numero: '))

def é_par(numero):
    if numero % 2 == 1:
        return False
    else:
        return True

é_par(numero)





