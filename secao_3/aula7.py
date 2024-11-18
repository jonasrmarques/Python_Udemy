"""
Variáveis são usadas para salvar algo na memória do computador
PEP8: inicie variáveis com letras minusculas, pode usar numéros e underline _.
O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a uma variável.
Uso: nome_variavel = expressão
"""

# nome_completo = "Jonas Rafael da Silva Marques";
# soma_dois_numeros = 2 + 2
# numero = int('1')

# print(numero, type(numero))
# print(nome_completo) # Jonas Rafael da Silva Marques
# print(soma_dois_numeros) # 4


nome = 'Jonas'
idade = 23
maior_de_idade = idade >= 18
resolucao = ""

if maior_de_idade == True:
    resolucao = "Sim ele é maior de idade"
else:
    resolucao = "Não, ele não é maior de idade"
                

print('Nome: ', nome, 'Idade: ', idade, "É maior de idade? ", resolucao)