'''Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.'''

lista = []

for n in range(11):
    x = int(input('digite um numero:'))
    lista.append(x)

for h in (range(10, 51, 1)):
    print(f'os números são: {h}')