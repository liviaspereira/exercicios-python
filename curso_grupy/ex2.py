primeiro = int(input('digite um numero:'))
segundo = int(input('digite um numero:'))
terceiro = int(input('digite um numero:'))

if primeiro > segundo:
    maior = primeiro
if primeiro > terceiro:
    maior = primeiro
if segundo > terceiro:
    maior = segundo
if terceiro > primeiro:
    maior = terceiro
if terceiro > segundo:
    maior = terceiro
print(f'maior: {maior}')