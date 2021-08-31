# delta < 0 nenhuma raiz real
# delta == 0 uma raiz real
# delta > 0 duas raizes reais
# delta = b²-4ac


print('Dada a equação f(x)= a*x²+b*x+c')
a = float(input('digite o valor de a:'))
b = float(input('digite o valor de b:'))
c = float(input('digite o valor de c:'))
delta = b*b -4*a*c
print(f'o valor de delta é: {delta}')

if delta > 0:
    print(input('há duas raizes reais'))
if delta < 0:
    print(input('não há nenhuma raiz real'))
if delta == 0:
    print(input('há uma única raiz real'))

