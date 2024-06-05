import zipfile
import csv
import json
import funcoesSite
from flask_paginate import Pagination
from dicionario import lerArquivo
from BTree import nomeOrdem, quantidadeOrdem,precoOrdem, pesquisarArvore, ordenarNoRange



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


def criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogo,  chave, tipo, valorMin, valorMax):

    if nomeAprocurar:
        catalogo = filtrarDicionario(catalogo, nomeAprocurar,  chave, tipo, valorMin, valorMax)
       # print("Filtrando catalogo. Resultado:")


    total = len(catalogo)
    #cprint("Total de itens no catalogo:", total)

    pagination_data = Organizar_Dados_Dentro_Da_Pagina(catalogo, (pagina - 1) * qtd_por_pagina, qtd_por_pagina, pagina - 1)
    #print("Dados da paginação:", pagination_data)

    paginacao = Pagination(page=pagina, total=total, per_page=qtd_por_pagina, search=False, format_number=True)
    
    return paginacao, pagination_data



def filtrarDicionario(dados,texto, chave, tipo, valorMin, valorMax):
    texto = texto.strip()
    novo_dicionario = pesquisarArvore(texto, dados)
    novo_dicionario_Ordenado = verificaOrdenacao(chave,tipo, novo_dicionario)

    if (chave == "Quantidade " or chave == "Preço ") and (valorMin != '' or valorMax != ''):
         print("Entrei na condição")
         ordenarNoRange(novo_dicionario_Ordenado, valorMin, valorMax)

    return novo_dicionario_Ordenado


def gerarDownload():
    path = 'arquivos/catalogo.json'
    csv_path = 'arquivos/catalogo_csv.csv'

    #Abre o arquivo JSON
    with open(path, 'r') as file:
        Arqui_JSON = json.load(file)

    # transforma json em csv

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
    
    
def verificaOrdenacao(chave, tipo, novoDicionario = None):
    catalogo = {}
    print("A chave é ", chave)
    if chave == "Nome " :
        print("Entrei no nome")
        catalogo = nomeOrdem(tipo, novoDicionario)
    elif chave == "Quantidade ":
        print("Entrei na uantidade")
        catalogo = quantidadeOrdem(tipo, novoDicionario)
    elif chave == "Preço ":
        print("Entrei no preco")
        catalogo = precoOrdem(tipo, novoDicionario)
    return catalogo

