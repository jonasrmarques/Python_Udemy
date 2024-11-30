"""
Introdução ao try/except
try ==> Tentar executar o código
except ==> Ocorreu algum erro ao tentar executar
"""

numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
    ...
except:
    print("Não é um número inteiro")
    ...

# if numero_str.isdigit():
# else: