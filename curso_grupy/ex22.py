'''Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
        idade média das mulheres
        idade média dos homens
        idade média do grupo'''

dicionario = {}
chave = 1
for n in range(3):
    chave = chave + 1
    idade = int(input('Digite sua idade: '))
    sexo = input("Qual seu sexo? (H ou M)")
    dicionario[chave] = [idade, sexo]
print(dicionario)
soma_homem = 0
soma_mulher = 0
soma_total = 0
total_mulher = 0
total_homem = 0
for w in dicionario.values():
    idade = w[0]
    sexo = w[1]
    if sexo == 'm':
        soma_mulher = soma_mulher + idade
        total_mulher = total_mulher + 1
    else:
        soma_homem = soma_homem + idade
        total_homem = total_homem + 1
soma_total = soma_homem + soma_mulher
media = soma_total / len(dicionario) 
if total_homem == 0:
    media_homem = 0
else:
    media_homem = soma_homem / total_homem
if total_mulher == 0:
    media_mulher = 0
else:
    media_mulher = soma_mulher / total_mulher
print(f'a media total é: {media} \nA media das mulheres é: {media_mulher} \nA media dos homens é: {media_homem}')