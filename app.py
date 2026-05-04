#Arquivo principal do sistema

from models.livro import Livro
from services.biblioteca_service import carregar_livro, salvar_livros

livros = carregar_livro()

print("====================================================                   =========================================================")
print("=================================================  Sistema de Biblioteca  ======================================================")
print("====================================================                   =========================================================")

print("Categoria padrão: ", Livro.categoria_padrao())

while True:
    print("\nMENU")
    print("1 - Cadastrar Livros")
    print("2 - Listar Livros")
    print("3 - Alterar Livros")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")

#Cadastrar livro

    if opcao == "1":
        print("\nCadastro de livro")

        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de Publicação: ")

        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        salvar_livros(livros)
        print("Livro Cadastrado!")

#Listar livros

    elif opcao == "2":
        print("\n Lista de Livros")
        if len(livros) == 0:
            print("Nenhum livro cadastrado")
        else:
            for i , livro in enumerate(livros):
                print("Livro", i)
                livro.exibir()

#Alterar Livro

    elif opcao == "3":
        for i, livro in enumerate(livros):
            print(i, '-', livro.titulo)
        pos = int(input(" Escolha o número do livro: "))
        novo = input(" Novo título: ")
        livros[pos].titulo = novo
        salvar_livros(livros)

#Sair do sistema
        

    elif opcao == "4":
        print("Encerrando o Sistema...")
        break
    else:
        print("Opção Inválida.")

