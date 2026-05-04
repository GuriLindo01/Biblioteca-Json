#Este arquivo contém funções responsáveis 
#Por salvar e carregar livros do JSON

import json
from models.livro import Livro

def carregar_livro():
    livros = []
    try:
        with open("livros.json", "r") as arquivos:
            dados = json.load(arquivos)
            livro = Livro(
                item["titulo"],
                item["autor"],
                item["ano"],
            )

            livros.append(livro)
    except:
        pass
    return livros

#Salvar livros
def salvar_livros(lista_livros):
    dados = []

    for livro in lista_livros:
        dados.append(livro.para_dict())
    with open("livros.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)