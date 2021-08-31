meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março' }
mes = int(input('digite um numero de 1 a 12'))

if mes in meses:
    print(f'o mês é: {meses.get(mes)}')
else:
    print('não existe')