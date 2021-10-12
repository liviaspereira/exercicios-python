'''Multiplicação de matriz por escalar'''

def soma_matriz (matriz1, escalar):
    linha = len(matriz1)
    coluna = len(matriz1[0])
    matriz3 = []
    for n in range(linha):
        matriz3.append([])
        for j in range(coluna):
            matriz3[n].append(0)

    for x in range(linha):
        for y in range(coluna):
            matriz3[x][y] = matriz1[x][y] * escalar
    return matriz3

print(soma_matriz([[1, 2], [3,4]], 3))