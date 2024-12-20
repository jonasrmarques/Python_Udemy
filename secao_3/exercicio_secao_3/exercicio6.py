"""
Iterando strings com while
"""

nome = "Jonas Rafael"
nova_string = ""
contador = 0

while contador < len(nome):
    
    letra = nome[contador]
    nova_string += f"*{letra}"
    contador+=1
    
nova_string += "*"
print(nova_string)