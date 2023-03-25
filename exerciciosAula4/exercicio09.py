# 9 - Crie uma lista contendo 5 nomes e adicione esta lista dentro da lista gerada no exercício 4


import random

lista1 = ['Maria', 'João', 'Marcio', 'Marta', 'Ana']
lista2 = []
contador = 0

while contador < 10:
    n = random.randint(10, 1580)
    lista2.append(n)
    contador += 1

lista2.append(lista1)
print(lista2)
