"""Receba dois números inteiros correspondentes à largura e altura. Devolva uma cadeia de caracteres "#" que representa um retângulo com as medidas fornecidas."""


largura = int(input("Digite um numero inteiro: "))
altura = int(input("Digite outro numero inteiro: "))

for i in range(altura):
    print("#" * largura)
    

