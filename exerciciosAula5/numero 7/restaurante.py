class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha

    def descreve_restaurante(self):
        print(f'Nome do restaurante: {self.nome}\nTipo de cozinha: {self.tipo_cozinha}')

    def abrir_restaurante(self):
        print('O restaurante esta aberto!')

    def fechar_restaurante(self):
        print('O restaurante esta fechado!')
