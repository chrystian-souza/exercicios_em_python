class Pessoa:
    def __init__(self, id, nome, idade, ):
        self.id = id
        self.nome = nome
        self.idade = idade

    def caminhar(self, quantidade_passos: int) -> str:
        return print(f'{self.nome} caminhou {quantidade_passos} passos.')

    def __str__(self):
        return print(f'\nId: {str(self.id)} \nNome: {str(self.nome)} \nIdade: {str(self.idade)}')
