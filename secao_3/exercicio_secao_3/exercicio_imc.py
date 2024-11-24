def imc (peso, altura):
    calculo = peso / altura ** 2
    
    conversao = (int(calculo * 10%10))
    print(conversao)
    
    if calculo >= 40.0:
        print("O bagulho ta doido pra tu, tu vai terminar morrendo, vai se cuidar")
    elif calculo >= 35.0 and calculo <= 39.0:
        print("Tas obeso grau 2, se tu não se cuidar tu vai cair na condição de cima e vai morrer")
    elif calculo >= 30.0 and calculo <= 34.9:
        print("Tas obeso grau 1, não ta tão lascado, mas ainda sim tem que se cuidar")
    elif calculo >= 25.0 and calculo <= 29.9:
        print("Tas com sobrepeso, vai correr pra ajustar isso ai")
    elif calculo >= 18.6 and calculo <= 24.9:
        print("Teu peso ta normal, fica peixe mas se cuida pra não cair na condição de cima")
    else:
        print("Tas abaixo do peso parceiro, vai comer")
    
    
    return calculo

imc(92, 1.75)
