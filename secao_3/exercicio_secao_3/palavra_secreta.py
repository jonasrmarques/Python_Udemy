"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

-Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    -Se a letra digitada estiver na palavra secreta, exiba a letra;
    -Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# palavra_secreta = "chocolate"
# letras_acertadas = ""

# while True:
#     tentativa = input("Digite uma letra: ")
    
#     if tentativa in palavra_secreta:
#         letras_acertadas += tentativa
        
    
#     palavra = ""
#     for letra in palavra_secreta:
#         if letras_acertadas in letra:
#             palavra += letra
#         else:
#             palavra+= "*"
            
#     print(palavra)
    



































palavra_secreta = "morango"
letras_acertadas = ''



while True:
    letra_digitada = input("Digite uma letra: ")
    
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada = "*"
        
    
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print(f"Parabéns, você acertou a palavra secreta, que era: {palavra_secreta}")
        break