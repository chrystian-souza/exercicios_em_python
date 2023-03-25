# 2 -  Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

lista = []
lista.append(input('Digite o nome de um numero 4: '))
lista.append(input('Digite o nome de outro numero 4: '))

print(lista)
print(f'tamanho da lista é: {len(lista)}')

if (lista[0] != lista[1]):
    print('Possuem conteúdo diferente. ')
else:
    print('Possuem conteúdo iguais. ')

if len(lista[0]) != len(lista[1]):
    print('Possuem tamanho diferente')
else:
    print('Possuem tamanho iguais')
