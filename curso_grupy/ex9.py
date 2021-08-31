#Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá 
# ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, 
# este deverá ser apresentado subtraindo-se 5.

x = float(input('Digite um número:'))
y = float(input('Digite outro número:'))
w = x + y
print(f'o valor de w é: {w}')
if w > 20:
    h = w + 20
    print(f'o valor de h é: {h}')
if w <= 20:
    j = w - 5
    print(f'o valor é: {j}')