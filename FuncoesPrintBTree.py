import pandas as pd
from BTree import BTree
from dicionario import lerArquivo
import os 

def limpar_terminal():
    # Verifica o sistema operacional e escolhe o comando apropriado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

def imprime(dicio, chave):
    posicao = 0
    print("POSICAO | ID | NOME | PRECO | QUANTIDADE")
    for id, item in dicio.items():
        print("Posicao {} : {} | {} | {} | {}".format(posicao+1, id, item["nome"], item["preco"], item["quantidade"]))
        posicao += 1

# Main Functionality
if __name__ == "__main__":
    
    data = lerArquivo()
    print("---- Escolha chave da arvore entre (nome, preco, quantidade, id): ")
    chave = input("Digite igual acima: ")
    
    arvore = BTree(3, chave)
    
    for id, item in data.items():
        if chave == "id":
            arvore.inserir(int(id))
        else:
            arvore.inserir(item[chave])
            
    if arvore is not None:
        while True:
            print("Enter para continuar!")
            print("\nEscolha uma opção:")
            print("1. Imprimir todos os registros")
            print("2. Imprimir registros menores que uma chave")
            print("3. Imprimir registros maiores que uma chave")
            print("4. Imprimir registros em um intervalo de chaves")
            print("5. Sair")
            opcao = int(input("Opção: "))
            dicio_novo = {}
            limpar_terminal()
            
            if opcao == 1:
                print("-------------------------------------------")
                print(" Ordenado pela chave - {}".format(chave))
                print("-------------------------------------------")
                dicio_novo = arvore.dicioOrdemCrescente(arvore.raiz, data, dicio_novo)
                imprime(dicio_novo, chave)
            elif opcao == 2:
                print("-------------------------------------------")
                print(" Ordenado pela chave - {}".format(chave))
                print("-------------------------------------------")
                if chave == "nome":
                    print("A chave nome nao possui minimo!")
                else:
                    key = int(input("Informe a chave: "))
                    dicio_novo = arvore.dicio_In_Range(arvore.raiz, data, dicio_novo, 0, key)
                    imprime(dicio_novo, chave)
            elif opcao == 3:
                print("-------------------------------------------")
                print(" Ordenado pela chave - {}".format(chave))
                print("-------------------------------------------")
                if chave == "nome":
                    print("A chave nome nao possui maximo!")
                else:
                    key = int(input("Informe a chave: "))
                    dicio_novo = arvore.dicio_In_Range(arvore.raiz, data, dicio_novo, key, 10000)
                    imprime(dicio_novo, chave)
            elif opcao == 4:
                print("-------------------------------------------")
                print(" Ordenado pela chave - {}".format(chave))
                print("-------------------------------------------")
                if chave == "nome":
                    print("A chave nome nao possui maximo!")
                else:
                    key1 = int(input("Informe o intervalo minimo: "))
                    key2 = int(input("Informe o intervalo maximo: "))
                    dicio_novo = arvore.dicio_In_Range(arvore.raiz, data, dicio_novo, key1, key2)
                    imprime(dicio_novo, chave)
            elif opcao == 5:
                break
            else:
                print("Opção inválida!")
