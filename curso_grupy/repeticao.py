"""Calcule o somatório dos números de 1 a 100 e imprima o resultado."""

soma = 0
lista = []
for i in range(0,101):
    soma += i
    lista.append(soma)
print(lista)