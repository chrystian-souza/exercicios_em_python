# 4 - Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
# de download do arquivo usando este link (em minutos).

arquivo = float(input('Informe o tamanho do arquivo em MB: '))
link = float(input('Informe a velocidade do link de internet em Mbps: '))

link = link / 8
link = arquivo / link
print(f'Levará  {round(link)} segundos para concluir o download. ')
