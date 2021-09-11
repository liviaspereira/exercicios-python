'''Crie uma função que receba um valor de temperatura em Fahrenheit e transforme em Celsius.

Relembrar é viver: (c/5) = ((f-12) / 9)'''

temperatura = float(input('Digite a temperatura em Fahrenheit: '))

def temperatura_em_celsius(temperatura):
    Celsius = (((5 * (temperatura - 32))) / 9)
    return Celsius 

print(temperatura_em_celsius(temperatura))
