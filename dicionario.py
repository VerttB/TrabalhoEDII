import json

def adicionarProdutoatalogo(dict, nome, quantidade, preco, descricao):
    id = len(dict)+1
    nova = dict(nome=nome, quantidade=quantidade, preco=preco, descricao=descricao)
    dict[id] = nova
    pass

def removerProduto(dict, id_delete):
    for id in dict:
        if(id_delete == id):
            dict[id].pop()

def modificarProduto(dict, ):
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