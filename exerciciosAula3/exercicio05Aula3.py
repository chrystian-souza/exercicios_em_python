# 5 - Faça um programa que calcule o número médio de alunos por
# turma. Para isto, peça a quantidade de turmas e a quantidade de
# alunos para cada turma. As turmas não podem ter mais de 40 alunos.

media = 0
contar_alunos = 0

qtd_turmas = int(input('Informe a qtd de turma: '))

for i in range(qtd_turmas):
    while True:
        alunos = int(input(f"Informe quantos alunos tem na turma: {i + 1}- "))
        if alunos <= 40:
            break
    contar_alunos = alunos + alunos
    media = alunos / qtd_turmas

print(f'Turmas {qtd_turmas} Alunos {contar_alunos} media dos alunos é {int(media)} por turma')
