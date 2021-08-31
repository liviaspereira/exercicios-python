# Ter entre 16 e 69 anos.
# Pesar mais de 50 kg.
# Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

tempo = (input('Você descansou mais que 6h nas ultimas 24h?:'))
if tempo == 'Nao':
    print('você não pode doar sangue:')
elif tempo == 'Sim':
    idade = int(input('Digite sua idade:'))
    peso = float(input('Digite seu peso:'))
    if idade >= 16 and idade <= 69 and peso >= 50:
        print('você pode doar sangue')
    else: 
        print('você não pode doar sangue')