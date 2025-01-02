numero_secreto = 10

tentativas = 0

while True:
    aposta = int(input("Digite um número que você acha que é o certo: "))
    if aposta == numero_secreto:
        print("Parabéns, você venceu!")
        tentativas+=1
        break
    elif aposta > numero_secreto:
        print("O número que você colocou é maior")
        tentativas+=1
        
    else:
        print("O número que você colocou é menor")
        tentativas+=1
        
    continuar = input("Deseja continuar?")
    
    if continuar != "s":
        break
    
print(f"Total de tentativas: {tentativas}")