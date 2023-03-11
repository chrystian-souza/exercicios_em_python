# 12 - Utilize a função criada no exercício anterior e mostre em tela a soma total de todos os valores de uma lista.

import Exercicio11

# print(Exercicio11.lista_num(9))

lista_num = Exercicio11.lista_num(9)

print(lista_num)
soma = 0
for i in lista_num:
    soma = i + soma

print(soma)

