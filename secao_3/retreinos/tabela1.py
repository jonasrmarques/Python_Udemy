tabela = int(input("Quantas colunas você deseja? "))

numero = 1

i = 0

while i < tabela:
    coluna = 1
    while coluna <= tabela:
        print(f"{numero:2}", end=" ")
        numero+=1
        coluna+=1
        continue
    print()
    i+=1