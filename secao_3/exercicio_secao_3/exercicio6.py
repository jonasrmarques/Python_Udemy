"""
Iterando strings com while
"""

nome = "Jonas Rafael"
nome_novo = ""

i = 0

while i < len(nome):
    letra = nome[i]
    nome_novo = nome_novo + f"*{letra}"
    
    i+=1


print(nome_novo)