# 1 - Remova strings vazias da lista de strings abaixo:
# lista_nomes = [‘Emanoela’, ‘Jonatan’, ‘’, ‘Kelly’, None, ‘Henrique’, ‘’]

# com metodo remove!
# lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']
#
# print("lista original: " + str(lista_nomes))
#
# while("" in lista_nomes):
#     lista_nomes.remove("")
#
# print('lista modificada' + str(lista_nomes))

# com medito pop!

lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']

for i in lista_nomes:
    if i == '' or i is None:
        print(f'Removendo o valor {i} no índice {lista_nomes.index(i)}')
        lista_nomes.pop(lista_nomes.index(i))

print(lista_nomes)
