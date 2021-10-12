'''Dado duas matriz, retorne a soma'''

def soma_matriz (matriz1, matriz2):
    linha = len(matriz1)
    coluna = len(matriz1[0])
    matriz3 = []
    for n in range(linha):
        matriz3.append([])
        for j in range(coluna):
            matriz3[n].append(0)

    for x in range(linha):
        for y in range(coluna):
            matriz3[x][y] = matriz1[x][y] + matriz2[x][y]
    return matriz3


print(soma_matriz([[1, 2], [3,4]], [[2,4],[6,8]]))


