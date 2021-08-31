'''Crie um programa que imprime no formato HH:MM todos os horários cuja hora e minuto são 
números primos.'''

#ver se a hora é primo (como? pegar todos os numeros antes 23 e ver se o resto 
# é zero)

horas = []
for teste in range(24):
    primo = True
    for n in range(2, teste):
        if teste % n == 0:
            primo = False
            break

    if primo:
        horas.append(teste)

minutos = []
for teste in range(60):
    primo = True
    for n in range(2, teste):
        if teste % n == 0:
            primo = False
            break

    if primo:
        minutos.append(teste)
        
for hora in horas:
    for minuto in minutos:
        print(f'{hora}:{minuto}')