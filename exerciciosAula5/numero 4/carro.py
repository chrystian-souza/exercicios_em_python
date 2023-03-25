class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_info(self):
        return print(f'Marca: {self.marca},\nModelo: {self.modelo},\nAno: {self.ano}\n')
