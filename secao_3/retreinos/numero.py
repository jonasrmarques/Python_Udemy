quantidade_de_colunas = int(input("Digite a quantidade de colunas: "))

linha = 1

valor = 1


while linha <= quantidade_de_colunas:
    coluna = 1
    while coluna <= quantidade_de_colunas:
        print(f"{valor:2}", end=" ")
        valor+=1
        coluna+=1
    print()
    linha+=1
print("Acabou")