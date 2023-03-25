# # 6 - CrieumaclasseLivroquetenhaosatributostítulo,autoreano.Crieummétodonaclasseparaimprimirasinformaçõesdolivro.
# CrieumaclasseBibliotecaquetenhaumalistadelivrosemétodosparaadicionareremoverlivrosdalista.
# CrieumobjetodaclasseBiblioteca,adicionealgunslivrosàlista,eimprimaasinformaçõesdoslivrosdalista.

import livro


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def mostra_detalhes_livros(self):
        for i in self.livros:
            print(f'O Título do livro é: {i.titulo} \n'
                  f'O Autor do livro é: {i.autor} \n '
                  f'O Ano do livro é: {i.ano} ')
