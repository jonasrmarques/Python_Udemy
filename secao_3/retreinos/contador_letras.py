nome = "Jonas Rafael da Silva Marques"

letra_que_mais_aparece = ""
quantidade_de_vezes = 0

for letra in nome:
    contar_letras = nome.count(letra)
    
    if contar_letras > quantidade_de_vezes:
        quantidade_de_vezes = contar_letras
        letra_que_mais_aparece = letra
        
    