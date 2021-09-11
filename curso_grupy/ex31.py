'''Faça uma função que calcule a área de um círculo. Insira o raio como argumento.

Dica: faça a importação de math e use pi de lá.
'''


raio = float(input('digite o raio do circulo: '))

from math import pi
def area_do_circulo(raio):
    area = pi * raio ** 2
    return area

print(area_do_circulo(raio))

