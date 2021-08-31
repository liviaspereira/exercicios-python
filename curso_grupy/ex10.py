# Leia um número e imprima a raiz quadrada do número caso 
# ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.


a = float(input('digite um numero:'))
if a >= 0:
    h = a ** 0.5
else:
    h = a * a 
print(f'a resposta é: {h}')