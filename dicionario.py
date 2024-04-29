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

def modificarProduto(dict, id_alterar, tipo, text):
    tipo_str = ['quantidade', 'preco']
    tipo = tipo - 2
    for id, produto in dict.items():
        if id == id_alterar:
            produto[tipo_str[tipo]] = text


def atualizarArquivo(dict):
    with open('arquivos/catalogo.json', 'w') as arquivo:
        arquivo.write(json.dump(dict)) 
    pass


def lerArquivo():
    dados = {}
    with open('arquivos/catalogo.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados


    if len(dict) == 0:
        print("O Dicionario está vazio")
    else:
        for chave, valores in sorted(dict.items()):
            print(chave, ":", valores)


    print("""
          1 - Adicionar ao dicionário
          2 - Listar Dicionario
          3 - Tirar do Dicionario
          4 - Salvar em Arquivo
          5 - Carregar Arquivo
          6 - Adicionar Relações
          7 - Buscar
          Diga a opção que voce quer.
          """)