texto = "Pythhhhhhhhhhhoooonn"

qtd_de_letras = 0
letra_que_mais_aparece = ""

for letra in texto:
    qtd = texto.count(letra)
    
    if qtd > qtd_de_letras:
        qtd_de_letras = qtd
        letra_que_mais_aparece = letra
    # print(f"{letra:3}{qtd_de_letras}")
    
print(qtd_de_letras, letra_que_mais_aparece)
    
