# 8 - Usando a função len() imprima em tela quantos caracteres cada item da lista gerada no exercício 4 possui:

import random

lista = []
contador = 0
while contador < 10:
    n = random.randint(10, 1580)
    lista.append(n)
    contador += 1
    print(len(str(n)), '-', n)

