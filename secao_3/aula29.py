"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

Linha 1 recebe 1
Linha 1 recebe 2
Linha 1 recebe 3
Linha 1 recebe 4
Linha 1 recebe 5
Linha 2 recebe 1
      ...
"""

contador = 5;

linha = 1;

while linha <= contador:
    
    coluna = 1;
    while coluna <= contador:
        
        print(f"Linha {linha} recebe {coluna}")
        
        coluna+=1
    
    linha+=1;
    
print("Acabaram as linhas")