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
    
    def monta_dicio(self, dicio, dicio_atual, dado):
        for item_id, produto in dicio.items():
            if produto[self.tipo] == dado:
                dicio_atual[item_id] = produto
        return dicio_atual
    
    def monta_dicio_range(self, dicio, dicio_atual, dado):
        for item_id, produto in dicio.items():
            if produto[self.tipo] == dado:
                dicio_atual[item_id] = produto
                return dicio_atual
        return dicio_atual
    
    def monta_dicio_range2(self, dicio, dicio_atual, dado):
        if self.tipo == "id":
            for item_id, produto in dicio.items():
                if item_id == dado:
                    dicio_atual[item_id] = produto
                    return dicio_atual
        else:
            for item_id, produto in dicio.items():
                if produto[self.tipo] == dado:
                    dicio_atual[item_id] = produto
                    return dicio_atual
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
    
    def dicio_In_Range(self, node, dicio, dicio_atual, cont, min, max):
        if node is not None:
            for i in range(len(node.key)):
                if not node.folha:
                    dicio_atual, cont = self.dicio_In_Range(node.filho[i], dicio, dicio_atual, cont, min, max)
                if min <= cont <= max:
                    dicio_atual = self.monta_dicio_range(dicio, dicio_atual, node.key[i])
                cont += 1
            if not node.folha:
                dicio_atual, cont = self.dicio_In_Range(node.filho[len(node.key)], dicio, dicio_atual, cont, min, max)
        return dicio_atual, cont
    
    
    
    # def monta_dicio(self, dicio, dicio_atual, dado):
    #     for item_id, produto in dicio.items():
    #         if produto[self.tipo] == dado:
    #             dicio_atual[item_id] = produto
    #     return dicio_atual
    
    def gerar_dicionario_ordenado(self, dicio):
        chaves_ordenadas = self.percorrer_em_ordem(self.raiz, [])
        dicio_atual = {}
        for chave in chaves_ordenadas:
            dicio_atual = self.monta_dicio(dicio, dicio_atual, chave)
        return dicio_atual

    def percorrer_em_ordem(self, node, resultado):
        if node is not None:
            for i in range(len(node.key)):
                if not node.folha:
                    self.percorrer_em_ordem(node.filho[i], resultado)
                resultado.append(node.key[i])
            if not node.folha:
                self.percorrer_em_ordem(node.filho[len(node.key)], resultado)
        return resultado


    # def imprimir_arvore(self, node, nivel=0):
    #     if node is not None:
    #         print("Nível", nivel, "Chaves:", node.key)
    #         for i in range(len(node.filho)):
    #             self.imprimir_arvore(node.filho[i], nivel + 1)
    
    
    
arvoreQtd = BTree(3, "quantidade")
arvoreNome = BTree(3, "nome")
arvorePreco = BTree(3, "preco")
arvorePesquisa = BTree(3, "nome")

catalogo = lerArquivo()
 
for id, item in catalogo.items():
    arvoreQtd.inserir(item[arvoreQtd.tipo])
    arvoreNome.inserir(item[arvoreNome.tipo])
    arvorePreco.inserir(item[arvorePreco.tipo])
    arvorePesquisa.inserir(item[arvorePesquisa.tipo])


def quantidadeOrdem(tipo):
    catalogoNovo = {}
    if(tipo == "crescente"):
        resultado = arvoreQtd.dicioOrdemCrescente(arvoreQtd.raiz, catalogo, catalogoNovo)
    else:  
        resultado = arvoreQtd.dicioOrdemDecrescente(arvoreQtd.raiz, catalogo, catalogoNovo)
    return resultado

def nomeOrdem(tipo):
    catalogoNovo = {}
    if(tipo == "crescente"):
        resultado = arvoreNome.dicioOrdemCrescente(arvoreNome.raiz, catalogo, catalogoNovo)
    else:  
        resultado = arvoreNome.dicioOrdemDecrescente(arvoreNome.raiz, catalogo, catalogoNovo)
    #print("Resiltadp", resultado)
    
    return resultado

def precoOrdem(tipo):
    catalogoNovo = {}
    if(tipo == "crescente"):
        resultado = arvorePreco.dicioOrdemCrescente(arvorePreco.raiz, catalogo, catalogoNovo)
    else:  
        resultado = arvorePreco.dicioOrdemDecrescente(arvorePreco.raiz, catalogo, catalogoNovo)
    #print("Resiltadp", resultado)
    
    return resultado


def pesquisarArvore(nome, dados):
    catalogoNovo = {}
    filtro = arvoreNome.pesquisaArvore(arvoreNome.raiz, dados, catalogoNovo, nome)
    print(filtro)
    return filtro