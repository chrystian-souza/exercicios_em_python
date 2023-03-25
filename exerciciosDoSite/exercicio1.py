# 01 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

contador = 0
lista = []
while (contador <= 3):
    n = float(input('Digite algum numero: '))
    lista.append(n)
    contador += 1
t = (lista[0] + lista[1] + lista[2] + lista[3]) / 2

print(t)
