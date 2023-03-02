# Questao 4

tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0
latas = int(litros/ 18.0)

if(litros % 18 != 0):
    latas += 1

print(f'Você devera comprar {latas} latas. ')
print(f'O custo total das tintas é r$ {float(latas * 80)}')