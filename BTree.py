from BTreeNode import BTreeNode
from dicionario import lerArquivo
class BTree:

    def __init__(self, grau, tipo):
        self.tipo = tipo
        self.grau = grau
        self.raiz = BTreeNode(grau, True)

    def inserir(self, valor):
        raiz = self.raiz
        if len(raiz.key) == 2 * self.grau - 1:
            temp = BTreeNode(self.grau, False)
            self.raiz = temp
            temp.filho.insert(0, raiz)
            temp.separaFilhos(0, raiz)
            temp.inserir_no(valor)
        else:
            raiz.inserir_no(valor)
    
    #--------------------------------------------------------
    
    def monta_dicio_range(self, dicio, dicio_atual, dado, min, max):
        if min < dado < max:
            for item_id, produto in dicio.items():
                if produto[self.tipo] == dado:
                    dicio_atual[item_id] = produto
            
        return dicio_atual
    
    def monta_dicio(self, dicio, dicio_atual, dado):
        if self.tipo == "id":
            for item_id, produto in dicio.items():
                if int(item_id) == dado:
                    dicio_atual[item_id] = produto
                    return dicio_atual
        else:
            for item_id, produto in dicio.items():
                if produto[self.tipo] == dado:
                    dicio_atual[item_id] = produto
        return dicio_atual
    
    # #--------------------------------------------------------
    
    def dicioOrdemCrescente(self, node, dicio, dicio_atual):
        if node is not None:  
            for i in range(len(node.key)):
                if not node.folha:
                    dicio_atual = self.dicioOrdemCrescente(node.filho[i], dicio, dicio_atual)  
                dicio_atual = self.monta_dicio(dicio, dicio_atual, node.key[i])  
            if not node.folha:
                dicio_atual = self.dicioOrdemCrescente(node.filho[len(node.key)], dicio, dicio_atual)  
        return dicio_atual
    
    def dicioOrdemDecrescente(self, node, dicio, dicio_atual):
        if node is not None:
            if not node.folha:
                dicio_atual = self.dicioOrdemDecrescente(node.filho[len(node.key)], dicio, dicio_atual)
            for i in range(len(node.key) - 1, -1, -1):
                dicio_atual = self.monta_dicio(dicio, dicio_atual, node.key[i])
                if not node.folha:
                    dicio_atual = self.dicioOrdemDecrescente(node.filho[i], dicio, dicio_atual)
        return dicio_atual
    
    def pesquisaArvore(self, node, dicio, dicio_atual, texto):
        if node is not None:
            if not node.folha:
                dicio_atual = self.pesquisaArvore(node.filho[len(node.key)], dicio, dicio_atual, texto)
            for i in range(len(node.key)):
                #print(node.key[i])
                if texto.upper() in node.key[i].upper():
                    dicio_atual = self.monta_dicio(dicio, dicio_atual, node.key[i])
                if not node.folha:
                    dicio_atual = self.pesquisaArvore(node.filho[i], dicio, dicio_atual, texto)
                    
        return dicio_atual
    
    def dicio_In_Range(self, node, dicio, dicio_atual, min, max):
        if node is not None:
            for i in range(len(node.key)):
                if not node.folha:
                    dicio_atual = self.dicio_In_Range(node.filho[i], dicio, dicio_atual, min, max)
                dicio_atual = self.monta_dicio_range(dicio, dicio_atual, node.key[i], min, max)
            
            if not node.folha:
                dicio_atual = self.dicio_In_Range(node.filho[len(node.key)], dicio, dicio_atual, min, max)
        
        return dicio_atual
    
    
    
arvoreQtd = BTree(3, "quantidade")
arvoreNome = BTree(3, "nome")
arvorePreco = BTree(3, "preco")

catalogo = lerArquivo()
 
for id, item in catalogo.items():
    arvoreQtd.inserir(item[arvoreQtd.tipo])
    arvoreNome.inserir(item[arvoreNome.tipo])
    arvorePreco.inserir(item[arvorePreco.tipo])

def idOrdem(tipo, novoDicionario):
    catalogoNovo = {}
    arvoreid2 = BTree(3,"id")
    print("Dicionario", novoDicionario)
    if novoDicionario is None:
        novoDicionario = lerArquivo()

    for id, item in novoDicionario.items():
        arvoreid2.inserir(int(id))

    if(tipo == "crescente"):
        resultado = arvoreid2.dicioOrdemCrescente(arvoreid2.raiz, novoDicionario, catalogoNovo)
    else:  
        resultado = arvoreid2.dicioOrdemDecrescente(arvoreid2.raiz, novoDicionario, catalogoNovo)

    return resultado


def quantidadeOrdem(tipo, novoDicionario):
    catalogoNovo = {}
    arvoreQtd2 = BTree(3,"quantidade")
    print("Dicionario", novoDicionario)
    if novoDicionario is None:
        novoDicionario = lerArquivo()

    for id, item in novoDicionario.items():
        arvoreQtd2.inserir(item[arvoreQtd2.tipo])

    if(tipo == "crescente"):
        resultado = arvoreQtd2.dicioOrdemCrescente(arvoreQtd2.raiz, novoDicionario, catalogoNovo)
    else:  
        resultado = arvoreQtd2.dicioOrdemDecrescente(arvoreQtd2.raiz, novoDicionario, catalogoNovo)

    return resultado

def nomeOrdem(tipo, novoDicionario):
    catalogoNovo = {}
    arvoreNome2 = BTree(3, 'nome')
    if novoDicionario is None:
        novoDicionario = lerArquivo()

    for id, item in novoDicionario.items():
        arvoreNome2.inserir(item[arvoreNome2.tipo])

    if(tipo == "crescente"):
        resultado = arvoreNome2.dicioOrdemCrescente(arvoreNome2.raiz, novoDicionario, catalogoNovo)
    else:  
        resultado = arvoreNome2.dicioOrdemDecrescente(arvoreNome2.raiz, novoDicionario, catalogoNovo)
    

    return resultado

def precoOrdem(tipo, novoDicionario):
    catalogoNovo = {}
    arvorePreco2 = BTree(3, 'preco')
    if novoDicionario is None:
        novoDicionario = lerArquivo()

    for id, item in novoDicionario.items():
        arvorePreco2.inserir(item[arvorePreco2.tipo])
    if(tipo == "crescente"):
        resultado = arvorePreco2.dicioOrdemCrescente(arvorePreco2.raiz, novoDicionario, catalogoNovo)
    else:  
        resultado = arvorePreco2.dicioOrdemDecrescente(arvorePreco2.raiz, novoDicionario, catalogoNovo)
    
    return resultado


def pesquisarArvore(nome, dados):
    catalogoNovo = {}
    filtro = arvoreNome.pesquisaArvore(arvoreNome.raiz, dados, catalogoNovo, nome)
    return filtro



def ordenarNoRange(dicionario, valorMin, valorMax, chave):
    dicionario_atual = {}
    print(f"valorMin:{type(valorMin)}:{valorMin}")
    print(f"valorMin:{type(valorMax)}:{valorMax}")
    arvorePrecoRange = BTree(3, 'preco')
    arvoreQtdRange = BTree(3,'quantidade')
    if dicionario is None:
        dicionario = lerArquivo()

    for id, item in dicionario.items():
        arvorePrecoRange.inserir(item[arvorePrecoRange.tipo])
        arvoreQtdRange.inserir(item[arvoreQtdRange.tipo])

    valorMax = 10000 if valorMax == '' else int(valorMax)
    valorMin = 0 if valorMin == '' else int(valorMin)
    print(valorMin)
    print(valorMax)
    if(chave == 'Quantidade '):
        resultado = arvoreQtdRange.dicio_In_Range(arvoreQtdRange.raiz, dicionario,dicionario_atual,valorMin,valorMax )
    elif( chave == 'Preço '):
        resultado = arvorePrecoRange.dicio_In_Range(arvorePrecoRange.raiz, dicionario,dicionario_atual,valorMin,valorMax )


    print(resultado)
    return resultado
