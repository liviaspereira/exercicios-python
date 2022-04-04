frutas = ["banana", "laranja", "maca"]
docinhos = ["brigadeiro", "ninho", "chocolate"]
feijoada = ["costelinha", "feijao", "tempero"]
listona = frutas + docinhos + feijoada
listona
quantidade_itens = len(listona)
for itens in range(quantidade_itens):
    del listona[0]
print(listona)
