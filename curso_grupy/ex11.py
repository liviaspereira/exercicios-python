# Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. 
# Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que
# não existe mês com este número.

print('Descubra o mês correspondente \o/')
mes = int(input('Digite um número de 1 a 12 e descubra o mês que corresponde:'))
if mes == 1:
    print('O mês é Janeiro')
elif mes == 2:
    print('O mês é Fevereiro')
elif mes == 3:
    print('O mês é Março')
elif mes == 4:
    print('O mês é Abril')
elif mes == 5:
    print('O mês é Maio')
elif mes == 6:
    print('O mês é Junho')
elif mes == 7:
    print('O mês é Julho')
elif mes == 8:
    print('O mês é Agosto')
elif mes == 9:
    print('O mês é Setembro')
elif mes == 10:
    print('O mês é Outubro')
elif mes == 11:
    print('O mês é Novembro')
elif mes == 12:
    print('O mês é Dezembro')
else:
    print('Digite um numero válido de 1 a 12')
