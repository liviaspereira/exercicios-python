'''Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de 
forma crescente ou False caso contrário.'''

lista = []

for n in range(5):
    x = int(input('digite um numero:'))
    lista.append(x)
print(f'a lista é:{lista}')
w = lista[0]
está_ordenada = 3


for k in lista[1:]:
    if w > k: 
        está_ordenada = False
        break
    w = k

if está_ordenada:
    print('A lista está ordenada!!')
else:
    print('A lista não está ordenada!!')