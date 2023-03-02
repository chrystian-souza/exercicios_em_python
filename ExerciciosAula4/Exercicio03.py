# 3 - Imprima os 10 primeiros números naturais após um número inserido no console usando um loop while:

num = int(input('Informe um número: '))
contador = 0

while (contador < 10):
    if num > 0:
        num += 1
        contador += 1
        print(num)
    else:
        print('erro!, não existem números naturais negativos')
        break



