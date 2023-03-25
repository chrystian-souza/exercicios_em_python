# 13 - Utilizando a função do exercício 11, imprima todos os números
# da lista como uma única string.

import exercicio11

var = Exercicio11.lista_num(10)
lista = []
for i in var:
    lista.append(str(i))
lista2 = ", ".join(lista)

print(lista2)

