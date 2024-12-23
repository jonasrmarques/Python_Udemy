string = "Esta é uma string novaeeeeeeeee"

qtd_de_vezes = 0
letra_que_mais_apareceu = ""

i = 0

while i < len(string):
    letra = string[i]
    letra_qtd = string.count(letra)
    
    if letra == " ":
        i+=1
        continue
    
    if letra_qtd > qtd_de_vezes:
        qtd_de_vezes = letra_qtd
        letra_que_mais_apareceu = letra
    
    i+=1
    
print(f"A letra que mais aparece é {letra_que_mais_apareceu}, e ela apareceu {qtd_de_vezes} vezes")