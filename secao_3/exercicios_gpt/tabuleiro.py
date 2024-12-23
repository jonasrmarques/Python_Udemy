numero = int(input("Digite um número inteiro diferente de 0"))

numero_total = 1;

linha = 1

while linha <= numero:
    coluna = 1
    while coluna <= numero:
        print(f"{numero_total:2}", end=" ")
        numero_total+=1
        coluna+=1
    print()
    linha+=1
    
0