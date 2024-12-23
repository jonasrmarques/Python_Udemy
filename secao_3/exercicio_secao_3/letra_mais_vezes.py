string = "Esta é uma string a ser contada"

letra_que_mais_aparece = ""
qtd_de_vezes = 0

i = 0


while i < len(string):
    
    contagem_de_letras = string[i]
    letras_que_se_repetem = string.count(contagem_de_letras)
    
    if contagem_de_letras == " ":
        i+=1
        continue

    if letras_que_se_repetem > qtd_de_vezes:
        qtd_de_vezes = letras_que_se_repetem
        letra_que_mais_aparece = contagem_de_letras

    i+=1
    
print(f"A letra que mais aparece é a {letra_que_mais_aparece} e ela se repete {qtd_de_vezes} vezes")