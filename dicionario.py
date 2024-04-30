import json

def adicionarProdutoatalogo(dict, nome, quantidade, preco, descricao):
    id = len(dict)+1
    nova = dict(nome=nome, quantidade=quantidade, preco=preco, descricao=descricao)
    dict[id] = nova
    pass

def removerProduto(dict, id_delete):
    if(id_delete in dict):
        dict.pop(id_delete)
        atualizarArquivo(dict)

def modificarProduto(dict, id_alterar, nome, quant, valor):
    for id, produto in dict.items():
        if id == id_alterar:
            produto['nome'] = nome
            produto['quantidade'] = quant
            produto['preco'] = valor
    atualizarArquivo(dict)


def atualizarArquivo(dict):
    with open('arquivos/catalogo.json', 'w') as arquivo:
        arquivo.write(json.dumps(dict)) 


def lerArquivo():
    dados = {}
    with open('arquivos/catalogo.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
