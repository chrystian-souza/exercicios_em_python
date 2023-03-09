# 14- Utilizando a função do exercício 11, crie uma lista,
# adicione a ela uma lista contendo 5 nomes e imprima todos os dados da
# lista como uma única string.

from Exercicio11 import lista_num

lista = lista_num(10)

lista1 = ['a', 'b', 'c', 'd', 'e']
lista.append(lista1)

lista2 = []
for i in lista:
    if type(i) == list:
        for a in i:
            lista2.append(str(a))
    else:
        lista2.append(str(i))

lista3 = ", ".join(lista2)
print(lista3)

