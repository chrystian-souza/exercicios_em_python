# 6 - Crie um programa que use uma iteração para exibir elementos  da
# lista gerada no exercício 4 presentes em posições de índice ímpares:

import random

lista = []
contador = 0

while contador < 10:
    n = random.randint(10, 1580)
    lista.append(n)
    contador += 1
for i in range(1, len(lista), 2):
    print(f'{i} - {lista[i]}')