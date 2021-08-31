'''Um supermercado está tendo muitos problemas com a validade de seus produtos e pediu sua ajuda com 
esse problema. Faça um programa que leia o dia, o mês e o ano da data atual e de validade de um 
produto, e imprima se o produto já está vencido ou não.'''

data_hoje = int(input('digite a data de hoje:'))
data_validade = int(input('digite a data de validade:'))
if data_validade < data_hoje:
    print('seu produto está vencido')
else:
    print('seu produto está lindão')

