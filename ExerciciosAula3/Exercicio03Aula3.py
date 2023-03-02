# 3 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

imp_consoantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(imp_consoantes)
var = []
for i in imp_consoantes:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        pass
    else:
        var.append(i)
print(len(var))
print(var)
