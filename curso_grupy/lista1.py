"""Receba uma lista com números inteiros. Verifique se a lista possui números repetidos, caso possua, exclua-os e devolva a lista alterada.

Dica 1: usar a função range.

Dica 2: ordene os elementos da lista em ordem ascendente."""


lista = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 10, 1, 3, 4]
numeros_unicos = []
for numeros in lista:
    if numeros not in numeros_unicos:
        numeros_unicos.append(numeros)
print(numeros_unicos)



    
        

