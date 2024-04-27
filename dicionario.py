import json

def adicionarProduto(dict, nome, quantidade, preco, descricao):
    id = len(dict)
    dict[id]
    pass
def removerProduto(id, dict):
    for id in dict:
        if(id == dict[id]):
            dict[id].pop()

def atualizarPesquisa():
    pass
def modificarProduto():
    pass
def atualizarArquivo(dict):
    with open('arquivos/catalogo.json', 'w') as arquivo:
        arquivo.write(json.dumps(dict)) 
    pass
def lerArquivo():
    dados = {}
    with open('arquivos/catalogo.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados