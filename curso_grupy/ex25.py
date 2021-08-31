'''Receba dois números inteiros correspondentes à largura e altura. 
Devolva uma cadeia de caracteres # que representa um retângulo com as medidas fornecidas.'''

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

soma = ''
for n in range(largura):
    soma += '#'

for h in range(altura):
    print(soma)