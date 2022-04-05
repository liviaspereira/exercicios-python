"""Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
        idade média das mulheres
        idade média dos homens
        idade média do grupo"""

homens = []
mulheres = []
total = []
for i in range(3):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ")
    total.append(idade)
    if sexo == "M":
        mulheres.append(idade)
    else:
        homens.append(idade)
print(f"A idade média do grupo é: {sum(total)/len(total)}")

if len(mulheres) == 0:
    print("Não há mulheres no grupo")
else:
    print(f"A idade média das mulheres é: {sum(mulheres)/len(mulheres)}")

if len(homens) == 0:
    print("Não há homens no grupo")
else:    
    print(f"A idade média dos homens é: {sum(homens)/len(homens)}")