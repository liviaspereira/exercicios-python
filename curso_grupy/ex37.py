'''Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver algum 
elemento que apareça mais de uma vez. Ela não deve modificar a lista original.'''


def has_duplicado(lista):
    for i in range(len(lista)-3):   
        for j in range(i+1, len(lista)-2):
            if lista[i] == lista[j]:
                return True
    return False
