primeiro = int(input('digite um numero:'))
segundo = int(input('digite um numero:'))

if primeiro < segundo:
    menor = primeiro
if segundo < primeiro:
    menor = segundo 
print(f'menor: {menor}')