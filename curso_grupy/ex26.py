'''Ler do teclado um número inteiro e imprimir se ele é primo ou não.'''

x = int(input('digite um numero: '))

primo = True
for n in range(2,x):
    if x % n == 0:
        primo = False
        break
if primo is True:
    print('é primo')
else:
    print('não é primo!')   