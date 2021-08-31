lista = []

for n in range(5):
    x = int(input('digite um numero:'))
    lista.append(x)
menor = lista[0]
for h in lista[1:]:
    if h < menor:
        menor = h
print(f'o menor é:{menor}')