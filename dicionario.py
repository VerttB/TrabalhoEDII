import json


def geraImagens():
    catalogo = lerArquivo()
    for item_id in catalogo.items():
        rota =  f"https://www.google.com/search?tbm=isch&q={catalogo[item_id]['nome']}"
        catalogo[item_id]["link"] = rota
    
    pass


def adicionarProdutoatalogo(dict, nome, quantidade, preco, descricao):
    # Verifica se o dicionário está vazio
    if not dict:
            id = '1'
    else:
        for i in dict:
            id = int(i)
    id+=1
    
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
    for id, produto in dict.items():
        if id == id_alterar:
            produto['nome'] = nome
            produto['quantidade'] = quant
            produto['preco'] = valor
    
    atualizarArquivo(dict)

def retirar_itens_comp(dicio, lista_carrinho):
    dicio_compra = {item['nome']: item for item in lista_carrinho}
    
    for nomeCarrinho, itemCarrinho in dicio_compra.items():
        for id, produto in dicio.items():
            if nomeCarrinho == produto['nome']:
                produto['quantidade'] -= itemCarrinho['quantidade']
    atualizarArquivo(dicio)
    
def atualizarArquivo(dicts):
    with open('arquivos/catalogo.json', 'w') as arquivo:
        arquivo.write(json.dumps(dicts, indent='\t')) 
    dicts = dict(sorted(dicts.items()))

def lerArquivo():
    dados = {}
    with open('arquivos/catalogo.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
