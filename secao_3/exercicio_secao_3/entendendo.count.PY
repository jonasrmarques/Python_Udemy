nome = "Jonass"

i = 0

while i < len(nome):
    letra = nome[i]
    contador = nome.count(letra)
    print(f"{letra}{contador}")
    
    i+=1
    