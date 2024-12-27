tabela = int(input("Digite quantas colunas sua tabela terá"))

valor = 1

linha = 1

while linha <= tabela:
    coluna = 1
    while coluna <= tabela:
        valor+=1
        print(f"{valor:2}", end=" ")
        coluna+=1
    linha+=1
    print()
