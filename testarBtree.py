import BTreeBiblioteca as bt

# Execução
Ap = None
chave = 1

# Menu
print("Bem-vindo, o que deseja realizar?")
menu = True
while menu:
    cmd = int(input("\nMenu de opções\n\n 0 - Sair\n 1 - Inserir\n 2 - Pesquisar\n 3 - Imprimir em-ordem\n 4 - Imprimir valores menores que uma chave\n 5 - Imprimir valores maiores que uma chave\n 6 - Imprimir menores Dataframe\n 7 - Imprimir maiores Dataframe\n 8 - Imprimir registros em um intervalo.\n\nEscolher:"))
    print("\n")
    if cmd == 0:
        print("Programa finalizado. ")
        menu = False
    elif cmd == 1:
        Ap, chave, df = bt.Inserir(Ap, chave)
    elif cmd == 2:
        reg = bt.Registro()
        reg.Chave = int(input("\nDigite uma chave maior que zero: "))
        reg = bt.Pesquisa(reg, Ap)
        if reg is not None:
            print(reg.Chave, "-", reg.Elemento)
    elif cmd == 3:
        bt.Imprime(Ap)
    elif cmd == 4:
        reg = bt.Registro()
        reg.Chave = int(input("\nDigite uma chave maior que zero: "))
        bt.ImprimeMenor(reg, Ap)
    elif cmd == 5:
        reg = bt.Registro()
        reg.Chave = int(input("\nDigite uma chave maior que zero: "))
        bt.ImprimeMaior(reg, Ap)
    elif cmd == 6:
        reg = bt.Registro()
        reg.Chave = int(input("\nDigite uma chave maior que zero: "))
        bt.ImprimeMenorDataFrame(reg, Ap, df)
    elif cmd == 7:
        reg = bt.Registro()
        reg.Chave = int(input("\nDigite uma chave maior que zero: "))
        bt.ImprimeMaiorDataFrame(reg, Ap, df)
    elif cmd == 8:
        bt.ImprimirRegistrosNoIntervalo(Ap)
    else:
        print("Comando inexistente.")
