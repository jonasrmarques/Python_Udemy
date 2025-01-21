from atividade import *


def cupom(cupom, valor):

    validacao = "123"
    if cupom == validacao:
        return (valor["valor"] * valor["quantidade"]) / 2
    else:
        return (valor["valor"] * valor["quantidade"] * 2)

def exibir2():
    validar = input("Qual o cupom?")
    dic = produtos()
    value = preco(dic)
    print(cupom(validar, value))
    exibir(dic, value)

exibir2()