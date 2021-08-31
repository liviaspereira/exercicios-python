'''Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
        idade média das mulheres
        idade média dos homens
        idade média do grupo'''

lista_homens = []
lista_mulheres = []

for n in range(3):
    idade = int(input('Digite sua idade: '))
    sexo = input("Qual seu sexo? (H ou M)")
    if sexo == 'm':
        lista_mulheres.append(idade)
    else:
        lista_homens.append(idade)
print(f'{lista_mulheres}')
print(f'{lista_homens}')

total_grupo = lista_mulheres + lista_homens
print(total_grupo)

soma_mulheres = 0
for idade_mulheres in lista_mulheres:
    soma_mulheres += idade_mulheres
media_mulheres = soma_mulheres / len(lista_mulheres)

soma_homens = 0
for idade_homens in lista_homens:
    soma_homens += idade_homens
media_homens = soma_homens / len(lista_homens)

media_grupo = (soma_mulheres + soma_homens) / len (lista_mulheres + lista_homens)

print(f'a media total é: {media_grupo} \nA media das mulheres é: {media_mulheres} \nA media dos homens é: {media_homens}')