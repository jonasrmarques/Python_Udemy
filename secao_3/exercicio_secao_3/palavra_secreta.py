"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

-Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    -Se a letra digitada estiver na palavra secreta, exiba a letra;
    -Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = "chocolate"

letra_acertada = ""

tentativas = 0

while True:
    letra_digitada = input("Digite apenas uma letra: ")
    tentativas += 1
    
    
    if len(letra_digitada) > 1:
        print("Por favor digite apenas uma letra")
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
        
        
    palavra_formada = "" 
    for letra in palavra_secreta:
        if letra in letra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += "*"
            
            
    print(palavra_formada)
            
    if palavra_formada == palavra_secreta:
        print(f"Parabéns, você acertou a palavra secreta!!, a palavra secreta era: {palavra_secreta} com um total de {tentativas} tentativas")
            