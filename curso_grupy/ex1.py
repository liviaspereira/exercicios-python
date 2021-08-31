def factorial(numero):
    if numero == 1 or numero == 0:
        return 1
    resultado = 1
    while numero > 1:
        resultado = resultado * numero
        numero = numero - 1
    return resultado
    
print(factorial(1000))