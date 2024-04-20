import json

def adicionarProduto():
    pass
def removerProduto():
    pass
def atualizarPesquisa():
    pass
def modificarProduto():
    pass
def atualizarArquivo():
    pass
def lerArquivo():
    dados = {}
    with open('arquivos/teste.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados