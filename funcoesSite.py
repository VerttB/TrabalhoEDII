
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



def filtrarDicionario(dados,texto=None):
    novo_dicionario = {}
    for item_id,item in dados.items():
        if texto is not None and texto in item['nome']:
            novo_dicionario[item_id] = item
    # print(novo_dicionario)
    return novo_dicionario
