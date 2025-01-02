numeros_positivos = 0

while True:
    
    for i in range(10):
        numero = int(input("Digite um número"))
        
        if numero > 0:
            numeros_positivos+=1

    print(f"O total de números positivos que você digitou foi: {numeros_positivos}")
    break