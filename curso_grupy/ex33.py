'''Utilizando a função anterior,
 faça a impressão da temperatura, em graus Celsius, de 0 °C a 100 °C, 
e todos os valores correspondentes em Fahrenheit.'''


def temperatura_F(celsius):
    F = ((9 * (celsius / 5))) + 32
    return F

for n in range(101):
    print(n, temperatura_F(n))