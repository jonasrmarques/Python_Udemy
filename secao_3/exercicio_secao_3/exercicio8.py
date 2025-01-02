"""
Faça uma lista de compras com listas

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.

Não permita que o programa quebre com erros de indices inexistens na lista

"""

lista_de_compras = []

while True:
    
    adicionar = input("O que você deseja adicionar na sua lista de compras? ").lower()
    if len(adicionar) > 1:
        lista_de_compras.append(adicionar)
    
    
    remover = input("Você deseja remover algum item? [S]im, [N]ão? ").lower()
    if remover == "s":
        escolha = input("Qual item você deseja remover?: ").lower()
        if escolha in lista_de_compras:
            lista_de_compras.remove(escolha)
        else:
            print("O item que você colocou, não está na lista, ou foi digitado errado!")
    
    

    listar = input("Você deseja visualizar os itens atuais da lista? [S]im ou [N]ão? ").lower()
    if listar == "s":
        print(lista_de_compras)
    
    
    continuar = input("Deseja continuar com a listagem de compras? [S]im, [N]ão ").lower()
    if continuar != "s":
        break
