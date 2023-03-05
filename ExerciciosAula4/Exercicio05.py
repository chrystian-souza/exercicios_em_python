# # 5 - Escreva um programa para exibir apenas os números da lista gerada no exercício 4 que
# satisfaçam as seguintes condições:
# - O número deve ser divisível por cinco
# - Se o número for maior que 95 e menor que 150 e, pule-o e passe para o próximo
# número
# - Se o número for maior que 1500, pare o loop

import random

lista = []
contador = 0
while contador < 10:
    n = random.randint(10, 1580)
    if n % 2 == 0:
        if n % 5 == 0:
            print(n),
            print("É par e divisível por 5")
    lista.append(n)
    contador += 1
    print(n)

