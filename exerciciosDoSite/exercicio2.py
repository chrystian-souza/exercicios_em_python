# 02 - Faça um Programa que converta metros para centímetros.

metros = float(input('Informe os metros: '))

centimetros = metros * 100

if metros == 1.0:
    print(f'{metros} metro equivale a: {centimetros} centimetros')
elif metros == 0.0:
    print(f'{metros} metro equivale a: {centimetros} centimetro')
else:
    print(f'{metros} metros equivale a: {centimetros} centimetros')
