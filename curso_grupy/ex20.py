'''Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
        idade média das mulheres
        idade média dos homens
        idade média do grupo'''

lista = []
for h in range(5):
    h = int(input('Digite sua idade: '))
    lista.append(h)
print(f'{lista}')
soma = 0
for i in lista:
    print(i)
    soma += i
print(f'{soma}')
media = soma / len(lista)
print(f'a média é: {media}')

