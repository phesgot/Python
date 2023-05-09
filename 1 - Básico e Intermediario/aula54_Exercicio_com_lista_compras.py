"""
Faça uma lista de compras com listas 
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com 
erros de indices inexistentes na lista.
"""
import os

lista_compras = []


while True:
    print("\nSelecione uma opção: ")
    opcao = input("[i]nserir   [a]pagar   [l]istar: ").lower()

    if opcao == 'i':
        os.system('cls')
        insercao = input("\nO que deseja inserir: ")
        lista_compras.append(insercao)
        print('Item inserido!')

    elif opcao == 'a':
        os.system('cls')
        try:
            indice = int(input("\nEscolha o indice a apagar: "))
            lista_compras.pop(indice)
            print("Item excluido!\n")
        except ValueError:
            print("\nInserir um indice de número inteiro.")
        except IndexError:
            print("\nO indice inserido não existe, tente outro.")

    elif opcao == 'l':
        os.system('cls')
        if lista_compras != []:
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
        else: 
            print("\nA lista está vazia.\n")
    
    else:
        print("\nVocê digitou uma opção invalida.")