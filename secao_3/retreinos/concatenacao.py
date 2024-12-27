nome = input("Digite seu nome: ")

nome_novo = ""

i = 0

while i < len(nome):
    letra = nome[i]
    nome_novo += f"*{letra}"
    
    i+=1
nome_novo += "*"

print(nome_novo)