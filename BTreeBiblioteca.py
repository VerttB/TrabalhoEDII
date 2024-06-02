import pandas as pd # pip install pandas
import openpyxl # pip install openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import string

# Declaração das classes e definição do grau da árvore
class Registro:
    def __init__(self):
        self.Chave = None
        self.Elemento = None

class Pagina:
    def __init__(self, ordem):
        self.n = 0
        self.r = [None for _ in range(ordem)]
        self.p = [None for _ in range(ordem+1)]

# Pesquisa
def Pesquisa(x, Ap):
    i = 1
    if Ap is None:
        print("Registro não está presente na árvore\n")
        return None

    while i < Ap.n and x.Chave > Ap.r[i - 1].Chave:
        i += 1
    if x.Chave == Ap.r[i - 1].Chave:
        x = Ap.r[i - 1]
        return x

    if x.Chave < Ap.r[i - 1].Chave:
        x = Pesquisa(x, Ap.p[i - 1])
    else:
        x = Pesquisa(x, Ap.p[i])

    return x

# Funções de inserção

# Insere o registro na página escolhida
def _InsereNaPagina(Ap, Reg, ApDir):
    k = Ap.n
    NaoAchouPosicao = (k > 0)
    while NaoAchouPosicao:
        if Reg.Chave >= Ap.r[k - 1].Chave:
            NaoAchouPosicao = False
            break
        Ap.r[k] = Ap.r[k - 1]
        Ap.p[k + 1] = Ap.p[k]
        k -= 1
        if k < 1:
            NaoAchouPosicao = False

    Ap.r[k] = Reg
    Ap.p[k + 1] = ApDir
    Ap.n += 1

# Busca a página onde o registro será inserido e controla a divisão de páginas por Overflow
def _Ins(Reg, Ap, Cresceu, RegRetorno, ApRetorno, Ordem):
    i = 1
    J = None
    if Ap is None:
        Cresceu = True
        RegRetorno = Reg
        ApRetorno = None
        return Cresceu, RegRetorno, ApRetorno

    while i < Ap.n and Reg.Chave > Ap.r[i - 1].Chave:
        i += 1

    if Reg.Chave == Ap.r[i - 1].Chave:
        print(" Erro: Registro já está presente\n")
        Cresceu = False
        return Cresceu, RegRetorno, ApRetorno

    if Reg.Chave < Ap.r[i - 1].Chave:
        i -= 1

    Cresceu, RegRetorno, ApRetorno = _Ins(Reg, Ap.p[i], Cresceu, RegRetorno, ApRetorno, Ordem)

    if not Cresceu:
        return Cresceu, RegRetorno, ApRetorno
    if Ap.n < Ordem: # Página tem espaço
        _InsereNaPagina(Ap, RegRetorno, ApRetorno)
        Cresceu = False
        return Cresceu, RegRetorno, ApRetorno

    # Overflow: Página tem que ser dividida
    ApTemp = Pagina(Ordem)
    ApTemp.n = 0
    ApTemp.p[0] = None
    if i < (Ordem // 2) + 1:
        _InsereNaPagina(ApTemp, Ap.r[Ordem - 1], Ap.p[Ordem])
        Ap.n -= 1
        _InsereNaPagina(Ap, RegRetorno, ApRetorno)
    else:
        _InsereNaPagina(ApTemp, RegRetorno, ApRetorno)
    for J in range((Ordem // 2) + 2, Ordem + 1):
        _InsereNaPagina(ApTemp, Ap.r[J - 1], Ap.p[J])
    Ap.n = (Ordem // 2)
    ApTemp.p[0] = Ap.p[(Ordem // 2) + 1]
    RegRetorno = Ap.r[(Ordem // 2)]
    ApRetorno = ApTemp
    return Cresceu, RegRetorno, ApRetorno

# Cria página da nova raiz caso a árvore cresça em altura
def _Insere(Reg, Ap, Ordem):
    Cresceu = False
    RegRetorno = Registro()
    ApRetorno = Pagina(Ordem)
    Cresceu, RegRetorno, ApRetorno = _Ins(Reg, Ap, Cresceu, RegRetorno, ApRetorno, Ordem)
    if Cresceu:
        ApTemp = Pagina(Ordem)
        ApTemp.n = 1
        ApTemp.r[0] = RegRetorno
        ApTemp.p[1] = ApRetorno
        ApTemp.p[0] = Ap
        Ap = ApTemp
    return Ap

# Insere elementos do arquivo
def _InserirElementos(Ap, ordem, dataframe, chave):
    tam_lin, tam_col = dataframe.shape
    for i in range(tam_lin): # 45 linhas
        reg = Registro()
        reg.Chave = dataframe.iloc[i, 0]
        reg.Elemento = i                 
        Ap = _Insere(reg, Ap, ordem)
        chave += 1
    return Ap, chave

# Define os registros a serem inseridos
def Inserir(Ap, chave):
    ordem = int(input("Digite a ordem da árvore: "))
    arq = input("Digite o nome do arquivo com a extenção: ")
    print(arq)
    input("pause!! ")
    if arq.lower().endswith(".csv"):
        dataframe = pd.read_csv(arq, header=None)      
    elif arq.lower().endswith((".xls", ".xlsx")):
        dataframe = pd.read_excel(arq, header=None)
    elif arq.lower().endswith(".json"):
        dataframe = pd.read_json(arq)
    else:
        print("Arquivo incompatível.")
        return Ap, chave, None
    # imprimindo dataframe criado do arquivo
    print("\nDataframe")
    print(dataframe)
    a = input("Digite um caractere para continuar")
    Ap, chave = _InserirElementos(Ap, ordem, dataframe, chave)
    return Ap, chave, dataframe

# Impressão
def Imprime(Ap):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            Imprime(Ap.p[i])
            print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
            i += 1
        Imprime(Ap.p[i])

def ImprimeMenor(x, Ap):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            ImprimeMenor(x, Ap.p[i])
            if Ap.r[i].Chave < x.Chave:
                print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
            i += 1
        ImprimeMenor(x, Ap.p[i])

def ImprimeMaior(x, Ap):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            ImprimeMaior(x, Ap.p[i])
            if Ap.r[i].Chave > x.Chave:
                print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
            i += 1
        ImprimeMaior(x, Ap.p[i])

# Impressão Arquivo Completo
# obtenção da chave na árvore B e restante dos dados do DataFrame
def ImprimeMenorDataFrame(x, Ap, df):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            ImprimeMenorDataFrame(x, Ap.p[i], df)
            if Ap.r[i].Chave < x.Chave:
                print(df.iloc[Ap.r[i].Elemento])
            i += 1
        ImprimeMenorDataFrame(x, Ap.p[i], df)

def ImprimeMaiorDataFrame(x, Ap, df):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            ImprimeMaiorDataFrame(x, Ap.p[i], df)
            if Ap.r[i].Chave > x.Chave:
                print(df.iloc[Ap.r[i].Elemento])
            i += 1
        ImprimeMaiorDataFrame(x, Ap.p[i], df)

# Nova função para imprimir registros em um intervalo de chaves
def ImprimeIntervalo(Ap, chave_inferior, chave_superior):
    if Ap is not None:
        i = 0
        while i < Ap.n:
            ImprimeIntervalo(Ap.p[i], chave_inferior, chave_superior)
            if chave_inferior <= Ap.r[i].Chave <= chave_superior:
                print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
            i += 1
        ImprimeIntervalo(Ap.p[i], chave_inferior, chave_superior)

# Função principal para obter intervalo do usuário e chamar ImprimeIntervalo
def ImprimirRegistrosNoIntervalo(Ap):
    chave_inferior = int(input("Digite a chave inferior do intervalo:"))
    chave_superior = int(input("Digite a chave superior do intervalo:"))
    print(f"Registros no intervalo [{chave_inferior}, {chave_superior}]:")
    ImprimeIntervalo(Ap, chave_inferior, chave_superior)

# Exemplo de uso das funções (Você pode comentar essas linhas em um ambiente de produção)
if __name__ == "__main__":
    Ap = None
    chave = 0
    Ap, chave, dataframe = Inserir(Ap, chave)
    ImprimirRegistrosNoIntervalo(Ap)