nome = input("Digite seu nome: ")

i = 0
nome_novo = ""

while i < len(nome):
    letra = nome[i]
    nome_novo += f"*{letra}"
    i+=1
nome_novo+="*"
print(nome_novo)