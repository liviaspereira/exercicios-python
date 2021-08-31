nomes_proximos = ['lucas', 'gato', 'livia']
frutas = ['maça', 'banana', 'morango']
doce = ['brigadeiro', 'bis', 'bolo']
listona = [nomes_proximos, frutas, doce]
print(listona)
listona[1].append('brigadeiro')
print(listona)
listona.append('coca')
print(listona)
del listona[0]
del listona[0]
del listona[0]
del listona[0]
print(listona)
compras = ['detergente', 'sorvete']
del compras[0]
del compras[0]
print(compras)
numeros = [45, 32, 1, 87, 2, 15]
numeros.sort()
print(numeros)
numeros_invertidos = numeros[::-1]
print(numeros_invertidos)