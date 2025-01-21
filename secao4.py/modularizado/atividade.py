def produtos():
    dados = [{
        "produto" : "sabão",
        "valor" : 12,
        "quantidade" : 2
    }, {
        "produto" : "pão",
        "valor" : 2,
        "quantidade" : 20
    }]

    return dados


def preco(n1):
    for item in n1:
        print(item["valor"] * item["quantidade"])
    

def exibir(produto, valor):
    
    cont=0
    for item in produto:
        print("o produto é:", item["produto"], "com o valor de:", valor[cont])
        cont+=1
        