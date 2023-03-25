class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return print(f'Seu nome é: {self.nome} \nSua idade é: {self.idade}')
