"Ler do teclado uma lista com 5 inteiros e imprimir o menor valor."

lista = []
for i in range(5):
    i = int(input(("Digite um numero inteiro: ")))
    lista.append(i)
    lista.sort()
menor = lista[0]
print(f"o menor numero é: {menor}")