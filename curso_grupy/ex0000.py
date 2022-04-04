from functools import total_ordering
from tomlkit import string


frase = "python é muito legal"
print(len(frase))
separacao = frase.split()
print(separacao)
total = []
for palavra in separacao:
    quantidade = len(palavra)
    total.append(quantidade)

print(f" A quantidade de cada palavra é: {total}")