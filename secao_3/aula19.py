"""
Operador lógico "not"
Usado para inverter expressões
not True = False
not False = True
"""

senha = input("Senha: ")

if senha == '123':
    print("Entrou")
elif not senha:
    print("Você não digitou nada")
else:
    print("Senha incorreta")