# Classe livro
# Esta classe representa um livro dentro do sistema

class Livro:
#Construtor
    def __init__(self, titulo, autor, ano):
#Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

#Propriedade (GETTER)
#Permite acessar o título mesmo sendo privado
    @property
    def titulo(self):
        return self.__titulo

#SETTER
#Permite alterar o título com validação
    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) < 2:
            print("Título inválido!")
        else:
            self.__titulo = novo_titulo

#Metodo para mostrar dados
    def exibir(self):
        self.__log()
        print("Título: ", self.__titulo)
        print("Autor: ", self.__autor)
        print("Ano: ", self.__ano)

#Metodo privado
    def __log(self):
        print("(LOG) Livro Acessado)")

#Converter para dicionário
#Necessário para salvar em JSON
    def para_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano,
        }
    
#Método estático
    @staticmethod
    def categoria_padrao():
        return "Literatura"