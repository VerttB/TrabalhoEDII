from BTreeNode import BTreeNode
import dicionario
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
            
    def monta_dicio(self, dicio, dicio_atual, dado):
        for item_id, produto in dicio.items():
            if produto[self.tipo] == dado:
                dicio_atual[item_id] = produto
        return dicio_atual
        
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
    
    # def dicio_In_Range():


arvoreNome = BTree(grau=5, tipo='nome')
arvoreId = BTree(grau=5, tipo='id')



catalogo = dicionario.lerArquivo()

for id, item in catalogo.items():
    arvoreNome.inserir(item['nome'])

#print(catalogo)
dicionarioAtual = {}

def precoOrdem():
    resultado = arvoreNome.dicioOrdemCrescente(arvoreNome.raiz,catalogo,dicionarioAtual)
   
    return resultado
