i = 1

try:
    numero = int(input("Digite um número para vermos a tabuada dele: "))
    operacao = input("Você deseja, somar, subtrair, multiplicar ou dividir?")
    while i <= 10:
        if numero >= 0 and numero <= 10:
            if(operacao == "somar"):
                print(f"Seu número {numero} somado por {i} é: {numero + i}")
                
            elif(operacao == "subtrair"):
                print(f"Seu número {numero} subtraido por {i} é: {numero - i}")
                
            elif(operacao == "multiplicar"):
                print(f"Seu número {numero} multiplicado por {i} é: {numero * i}")
                
            elif(operacao == "dividir"):
                print(f"Seu número {numero} dividido por {i} é: {numero // i}")
                
            else:
                print("Digite: 'somar', 'subtrair', 'multiplicar' ou 'dividir'")
            i+=1
except:
    print("Por favor, digite um número inteiro válido")