# 7 - Usando a função len() imprima em tela quantos itens existem na lista gerada noexercício 4:

import random

lista = []
contador = 0

while contador < 10:
    n = random.randint(10, 1580)
    lista.append(n)
    contador += 1

print(len(lista))
