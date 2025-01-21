def pessoa(**kwargs):
    
    pessoa2 = {
        "nome": kwargs.get("nome", "nada"),
        "idade": kwargs.get("idade", 23),
        "peso": kwargs.get("peso", 100)
    }
    return pessoa2

print(pessoa(nome="Jonas", idade=23, peso=92.2))

