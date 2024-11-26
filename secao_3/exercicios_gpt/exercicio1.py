"""
Exercício: Classificando um número

Crie um programa que peça para o usuário digitar um número inteiro e, em seguida, faça o seguinte:

Verifique se o número é positivo, negativo ou zero.
Informe ao usuário se o número é par ou ímpar.    
"""

numero = int(input("Digite um número inteiro"))

if numero % 2  == 0 and numero >= 1:
    print(f"O número {numero} é par e inteiro positivo")
elif numero % 2 != 0 and numero >= 1:
    print(f"O número {numero} é impar e inteiro positivo")
elif numero == 0:
    print(f"O número {numero} é zero")
elif numero % 2 == 0 and numero <= -1:
    print(f"O número {numero} é negativo e par")
else:
    print(f"O número {numero} é negativo e impar")