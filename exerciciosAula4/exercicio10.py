# 10 - Crie um programa para remover tudo que não for do tipo inteiro da lista gerada no exercício 9.

import random

lista1 = ['Maria', 'João', 'Marcio', 'Marta', 'Ana']
lista2 = []
contador = 0

while contador < 10:
    n = random.randint(10, 1580)
    lista2.append(n)
    contador += 1

lista2.append(lista1)
print(type(lista2))

for i in lista2:
    if type(i) == list:
        for a in range(len(i), 0, -1):
            i.pop(a-1)
            print(i)
print(lista2)



