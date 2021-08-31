'''Calcule a tabuada do 13.'''

print('VAMOS DESCOBRIR AS TABUADAS')
x = (int(input('Digite a tabuada que você quer saber:')))

for n in range(1, 11):
    h = x * n
    print(f'o resultado de {x}*{n} = {h}')
