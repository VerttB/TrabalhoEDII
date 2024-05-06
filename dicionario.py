import json

def adicionarProdutoatalogo(dict, nome, quantidade, preco, descricao):
    # Verifica se o dicionário está vazio
    if not dict:
            id = '1'
    else:
        for i in dict:
            id = int(i)
    id+=1
    preco = float(preco)
    quantidade = int(quantidade)
    
    print(f"O id é o seguinte {id}" )
    novo_produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco,
        'descricao': descricao
    }
    
    dict[str(id)] = novo_produto
    print(dict[str(id)])
    atualizarArquivo(dict)

def removerProduto(dict, id_delete):
    if(id_delete in dict):
        dict.pop(id_delete)
        atualizarArquivo(dict)

def modificarProduto(dict, id_alterar, nome, quant, valor):
    valor = float(valor)
    quant = int(quant)
    for id, produto in dict.items():
        if id == id_alterar:
            produto['nome'] = nome
            produto['quantidade'] = quant
            produto['preco'] = valor
    
    atualizarArquivo(dict)


def atualizarArquivo(dicts):
    with open('arquivos/catalogo.json', 'w') as arquivo:
        arquivo.write(json.dumps(dicts, indent='\t')) 
    dicts = dict(sorted(dicts.items()))

def lerArquivo():
    dados = {}
    with open('arquivos/catalogo.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
