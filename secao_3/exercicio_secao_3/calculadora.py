calculadora = "continuar"

while calculadora == "continuar":
    
    try:
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um segundo número: "))
        equacao = input("Digite qual operação você deseja: ")

        if equacao == "somar":
            soma = numero1 + numero2;
            print(f"A soma dos dois números é: {soma}")
        elif equacao == "subtracao":
            subtracao = numero1 - numero2;
            print(f"A soma dos dois números é: {subtracao}")
        elif equacao == "multiplicacao":
            multiplicacao = numero1 * numero2;
            print(f"A soma dos dois números é: {multiplicacao}")
        elif equacao == "divisao":
            divisao = numero1 / numero2;
            print(f"A soma dos dois números é: {divisao}")
        else:
            print("Digite um número inteiro")
        
        continuar = input("Deseja continuar? ")
        continuar.lower()
        if(continuar == "sim"):
            calculadora = "continuar"
        else:
            calculadora = "sair"
    except:
        print("Digite apenas números")