import zipfile
import csv
import json
import funcoesSite
from flask_paginate import Pagination
from dicionario import lerArquivo
from BTree import nomeOrdem, quantidadeOrdem,precoOrdem



def Organizar_Dados_Dentro_Da_Pagina(dados, inicio, qtd_por_pagina, pagina):
    novo_dicionario = {}
    tam = 0
    jump = 0

    for item_id, item in dados.items():
        inicio+=1
        if pagina != 0 and jump < (qtd_por_pagina * pagina):
            jump+=1
            continue
        
        novo_dicionario[item_id] = item
        tam+=1
        
        if tam == qtd_por_pagina: break
        
    return novo_dicionario


# def criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogo):
    
#     if catalogo is None:
#         catalogo = lerArquivo()
#         print("Entrei onde n devia")

#     if(nomeAprocurar is not None and nomeAprocurar != ''):
#         catalogo = filtrarDicionario(catalogo, nomeAprocurar)

#     total = len(catalogo)
#     pagination_data = Organizar_Dados_Dentro_Da_Pagina(catalogo, (pagina - 1) * qtd_por_pagina, qtd_por_pagina, pagina-1)
    
#     paginacao = Pagination(page=pagina, total=total, qtd_per_page=qtd_por_pagina, per_page = qtd_por_pagina,search =False, format_number=True)
    
#     return paginacao, pagination_data
    

def criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogo):
    if catalogo is None:
        catalogo = lerArquivo()
        #print("Entrei onde não devia. Catalogo lido:")

    if nomeAprocurar:
        catalogo = filtrarDicionario(catalogo, nomeAprocurar)
       # print("Filtrando catalogo. Resultado:")

    total = len(catalogo)
    #cprint("Total de itens no catalogo:", total)

    pagination_data = Organizar_Dados_Dentro_Da_Pagina(catalogo, (pagina - 1) * qtd_por_pagina, qtd_por_pagina, pagina - 1)
    #print("Dados da paginação:", pagination_data)

    paginacao = Pagination(page=pagina, total=total, per_page=qtd_por_pagina, search=False, format_number=True)
    
    return paginacao, pagination_data



def filtrarDicionario(dados,texto=None):
    novo_dicionario = {}
    for item_id,item in dados.items():
       #nome = item['nome'].upper()
        if texto is not None and texto.upper() in item['nome'].upper():
            novo_dicionario[item_id] = item
            
    return novo_dicionario


def gerarDownload():
    path = 'arquivos/catalogo.json'
    csv_path = 'arquivos/catalogo_csv.csv'

    #Abre o arquivo JSON
    with open(path, 'r') as file:
        Arqui_JSON = json.load(file)

    #Transforma JSON em CSV

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'quantidade', 'preco', 'descricao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for key, value in Arqui_JSON.items():
            writer.writerow({'id': key, 'nome': value['nome'], 'quantidade': value['quantidade'], 'preco': value['preco'], 'descricao': value['descricao']})

    #Gera arquivo ZIP
    zip_path = 'arquivos/catalogo.zip'
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(path, 'catalogo.json')
        zipf.write(csv_path, 'catalogo_csv.csv')

    return zip_path
    
    
def verificaOrdenacao(chave, tipo):
    catalogo = {}
    print("A chave é ", chave)
    if chave == "Nome " :
        print("Entrei no nome")
        catalogo = nomeOrdem(tipo)
    elif chave == "Quantidade ":
        print("Entrei na uantidade")
        catalogo = quantidadeOrdem(tipo)
    elif chave == "Preço ":
        print("Entrei no preco")
        catalogo = precoOrdem(tipo)
    return catalogo

