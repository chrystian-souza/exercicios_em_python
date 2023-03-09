# 11- Utilizando os códigos criados na resolução dos exercícios anteriores,
# crie uma função que retorne uma lista de itens inteiros e que receba a
# quantidade de itens a serem gerados por parâmetro.
import random


def lista_num(qtd):
    contador = 0
    inteiros = []
    while contador < qtd:
        n = random.randint(10, 1580)
        inteiros.append(n)
        contador += 1

    return inteiros

if __name__ == '__main__':
    print(lista_num(8))






