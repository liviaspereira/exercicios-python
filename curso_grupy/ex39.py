'''Escreva uma função que imprime todos os números primos entre 1 e 50
Dica: um número é primo se ele for divisível apenas por 1 e ele mesmo, use o operador % 
(resto da divisão) para isso.'''


def imprime_primo():
    for num in range(2,50):
        primo = True
        for i in range(2,num):
            if num % i == 0:
                primo = False
                break
        if primo is True:
            print(num)   


imprime_primo()
