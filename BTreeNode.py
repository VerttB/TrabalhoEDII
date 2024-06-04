class BTreeNode:
    # key são os nossos valores da arvore

    # Define os atributos padrão do node da arvoreB
    def __init__(self, ordem, folha = False):
          self.ordem = ordem
          self.folha = folha
          self.index = 0
          self.filho = []
          self.key = []

    # def inserir_no(self, key):
    #     i = len(self.key)-1 # i recebe a quantidade de valores que tem no nó
    #     if self.folha:
    #         self.key.append(0)
    #         while i >= 0 and self.key[i] > key:
    #             self.key[i+1] = self.key[i]
    #             i -= 1
    #         self.key[i+1] = key

    #     else:
    #         while i >= 0 and self.key[i] > key:
    #             i -= 1
    #         if len(self.filho[i+1].key) == 2 * self.ordem - 1:
    #             self.separaFilhos(i + 1, self.filho[i + 1])
    #             if self.key[i + 1] < key:
    #                 i += 1
    #         self.filho[i + 1].inserir_no(key)
    
    def inserir_no(self, key):
        i = len(self.key) - 1
        if self.folha:
            self.key.append(None)
            while i >= 0 and self.key[i] > key:
                self.key[i + 1] = self.key[i]
                i -= 1
            self.key[i + 1] = key
        else:
            while i >= 0 and self.key[i] > key:
                i -= 1
            i += 1
            if len(self.filho[i].key) == 2 * self.ordem - 1:
                self.separaFilhos(i, self.filho[i])
                if self.key[i] < key:
                    i += 1
            self.filho[i].inserir_no(key)
                  

    def separaFilhos(self, i, noFilho):
        noNovo = BTreeNode(noFilho.ordem, noFilho.folha) # Cria um novo nó
        self.filho.insert(i+1, noNovo) # Nó pai aponta para o novo nó
        self.key.insert(i, noFilho.key[self.ordem - 1]) # Move a chave mediana para o nó pai
        noNovo.key = noFilho.key[self.ordem:(2 * noFilho.ordem - 1)] # Move as chaves depois da mediana do filho para o novo no
        noFilho.key = noFilho.key[0:(self.ordem - 1)] # O noFilho mantem as chaves até ordem -1
        if not noFilho.folha:
             noNovo.filho = noFilho.filho[self.ordem:(2 * noFilho.ordem)]
             noFilho.filho = noFilho.filho[0:self.ordem]