"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados
Retorne o total para uma varipavel e mostre o valor da variável

Crie uma função que fala se um número é par ou impar
Retorne se o número é par ou impar
"""

def multiplicacao(*args):
    multiplicador = 1
    for numeros in args:
        multiplicador *= numeros
    return multiplicador

variavel = multiplicacao(1, 2, 3, 5)
# print(variavel)

#

def par_ou_impar(*args):
    
    for numeros in args:
        if numeros % 2 == 0:
            print(f"{numeros} é par") 
        else:
           print(f"{numeros} é impar")
    return "Acabooou"
pares_ou_impares = par_ou_impar(2, 3, 4, 5, 6)
print(pares_ou_impares)