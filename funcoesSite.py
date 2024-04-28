
def get_pagina(dados, inicio, qtd_por_pagina, pagina):
        novo_dicionario = {}
        inicio+=1 #O indice tem que começar em 1
        # fim = inicio + qtd_por_pagina
        # i = 0 #(qtd_por_pagina * pagina) + 1
        # for item_id, item in dados.items():
        #   if inicio <= i < fim:
        #     print(f'valor de i {i}')
        #     novo_dicionario[item_id] = item
        #     i+=1
            
        # print(novo_dicionario)
        # return novo_dicionario
        i = 1
        print(dados)
        while(len(novo_dicionario) < 15):
            if inicio <= i < qtd_por_pagina:
                novo_dicionario[str(i)] = dados[str(i)].items()
            if len(dados) == i:
                break
            i+=1
        print(novo_dicionario)
        return novo_dicionario
# def get_pagina(dados, inicio, qtd_por_pagina):
#     novo_dicionario = {}
#     tam = 0
        
#     for item_id, item in dados.items():
#         inicio+=1
#         if inicio < int(item_id) or inicio == int(item_id):
#             while inicio == int(item_id): inicio+=1
#             novo_dicionario[item_id] = item
#             tam+=1
#         if inicio > int(item_id): inicio-=1
#         if tam == qtd_por_pagina : break
    
#     return novo_dicionario

# def get_pagina(dados, inicio, qtd_por_pagina):
#     novo_dicionario = {}
#     tam = 0
    
#     for item_id, item in dados.items():
#         if inicio <= int(item_id) < inicio + qtd_por_pagina:
#             novo_dicionario[item_id] = item
#             tam += 1
#             if tam == qtd_por_pagina:
#                 break
    
#     return novo_dicionario

def filtrarDicionario(dados,texto=None):
    novo_dicionario = {}
    for item_id,item in dados.items():
        if texto is not None and texto in item['nome']:
            novo_dicionario[item_id] = item
    print(novo_dicionario)
    return novo_dicionario
