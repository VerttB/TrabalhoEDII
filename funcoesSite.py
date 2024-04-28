
def get_pagina(dados, inicio, qtd_por_pagina):
    novo_dicionario = {}
    inicio+=1 #O indice tem que começar em 1
    for item_id, item in dados.items():
        if inicio <= int(item_id) < (inicio + qtd_por_pagina):
            novo_dicionario[item_id] = item
    return novo_dicionario

def filtrarDicionario(dados,texto=None):
    novo_dicionario = {}
    for item_id,item in dados.items():
        if texto is not None and texto in item['nome']:
            novo_dicionario[item_id] = item
    return novo_dicionario
