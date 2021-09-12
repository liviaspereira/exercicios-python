'''Dada a função: y = 5x+2,determine os valores de y para x entre -10 a +10, onde x é inteiro'''


def funcaoy(x):
    y = 5 * x + 2
    return y


for x in range(-10, 10):
    print(x, funcaoy(x))
