from biblioteca import Biblioteca
from livro import Livro

minha_bib = Biblioteca()
livro1 = Livro('As Cronicas de Narnia', 'CS Lewis', 1994)
livro2 = Livro('O imbecil coletivo', 'Olavo e Carvalho', 2020)
livro3 = Livro('Python para iniciantes', 'Chrystian', 2023)

lista_livros = [livro1, livro2, livro3]

for liv in lista_livros:
    minha_bib.adicionar_livro(liv)

minha_bib.mostra_detalhes_livros()

