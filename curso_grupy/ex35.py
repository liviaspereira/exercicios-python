'''Crie uma função que receba 3 valores e calcula as raízes da fórmula de Bhāskara.

Dica: raiz quadrada é sqrt(), importando math: math.sqrt()'''

from math import sqrt

a = float(input("Digite o valor para a: "))
b = float(input("digite o valor para b: "))
c = float(input("digite o valor para c: "))


def bascara(a, b, c):
    if a == 0:
        return
    delta = b * b - 4 * a * c
    if delta < 0:
        return
    else:
        x1 = (-b + (sqrt(delta))) / (2 * a)
        x2 = (-b - (sqrt(delta))) / (2 * a)
        return x1, x2


print(bascara(a, b, c))
