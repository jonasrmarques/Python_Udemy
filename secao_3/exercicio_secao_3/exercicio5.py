"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input("Digite um número inteiro: "))  
    if numero % 2 == 0:
        print("É um número par")
    else:
        print("É um número impar")
except:
    print("Digite apenas um número inteiro")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario = int(input("Digite a sua hora"))
    if(horario <= 11 and horario >= 0):
        print("Bom dia")
    elif(horario <= 17 and horario >= 12 ):
        print("Boa tarde")
    elif(horario <= 23 and horario >= 18):
        print("Boa noite")
    else:
        print("Digite uma hora válida")
except:
    print("Digite apenas a hora, somente a hora")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >=5 or len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")