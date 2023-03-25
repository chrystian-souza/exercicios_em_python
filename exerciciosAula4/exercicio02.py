# 2 - Imprima as palavras que contenham letras e números juntos da frase abaixo:
# frase = 'Paulo é d4veloper e um b0m musico'

frase = 'Paulo é d4veloper e um b0m musico'

palavras = frase.split()
letras_e_num = []

for palavra in palavras:
    ver_letra = False
    ver_numero = False

    for letra in palavra:

        if letra.isdigit():
            ver_numero = True

        elif letra.isalpha():
            ver_letra = True
    if ver_numero == True and ver_letra == True:
        letras_e_num.append(palavra)
print(letras_e_num)
