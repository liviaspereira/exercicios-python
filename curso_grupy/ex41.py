'''Escreva uma função que retorne uma lista com todas as chaves de um dicionário que contém um 
certo valor.

Por exemplo, se o dicionário for {'a': 1, 'b': 2, 'c': 1, 'd': 4}, a função deve retornar
 ['a', 'c'] caso procure pelo valor 1; [] caso procure pelo valor 666.'''

def lista_dicionario(dicionario, valor):

    lista = []
    for chave, coisa in dicionario.items():
        if coisa == valor:
            lista.append(chave)
    return lista

print(lista_dicionario({'a': 1, 'b': 2, 'c': 2, 'd': 2}, 2))


  

        