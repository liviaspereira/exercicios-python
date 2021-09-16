'''Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. 
Escreva uma função chamada is_anagram que tome duas strings e retorne True se forem anagramas ou 
False caso contrário.'''

def is_anagram(string, string1):

    if len(string) != len(string1):
        return False

    lista = []
    for letra in string:
        lista.append(letra)
    
    lista1 = []
    for letra1 in string1:
        lista1.append(letra1)

    for letra in lista:
        if letra in lista1:
            lista1.remove(letra)
        else:
            return False
    return True

    