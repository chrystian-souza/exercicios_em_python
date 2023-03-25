# 4 - Escreva um programa que gere uma lista com 10 números aleatórios entre 20 e 1580:(utilize a lib random)

import random

lista = []
contador = 0
while contador < 10:
    n = random.randint(10, 1580)
    lista.append(n)
    contador += 1

print(lista)
