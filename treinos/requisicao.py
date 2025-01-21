import requests



url = "https://jsonplaceholder.typicode.com/users"


def conexao():
    res = requests.get(url)
    return res


def verificar_conexao(argumento):
    
    if argumento.status_code == 200:
        aviso = "Foi feito com sucesso a conexão"
        print(aviso)
        return aviso
    else:
        aviso = "A conexão não foi feita!"
        print(aviso)
        return aviso


def lista_com_nomes(argumento):
    lista = argumento.json()
    return lista

def nomes_emails(argumento):
    for nome in argumento:
        print(f"O nome do nosso usuário é: {nome["name"]} e ele(a) tem o email: {nome["email"]}")

def chamada_das_funcoes():
    lista_ = conexao()
    verificar_conexao(lista_)
    lista_com_dics = lista_com_nomes(lista_)
    nomes_emails(lista_com_dics)
    return lista_com_dics



chamada_das_funcoes()