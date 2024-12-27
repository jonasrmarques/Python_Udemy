palavra = "Olá, eu sou uma palavra que vai ser contada em um loop"

palavra_que_se_repete = ""
quantas_vezes_se_repete = 0

contador = 0


while contador < len(palavra):
    
    letra = palavra[contador]
    numero_de_vezes_que_se_repete = palavra.count(letra)
    
    if letra == " ":
        contador+=1
        continue
    
    if numero_de_vezes_que_se_repete > quantas_vezes_se_repete:
        quantas_vezes_se_repete = numero_de_vezes_que_se_repete
        palavra_que_se_repete = letra
    
    
    contador+=1

print(f"A letra que mais se repete é: {palavra_que_se_repete} em um total de {quantas_vezes_se_repete} vezes")