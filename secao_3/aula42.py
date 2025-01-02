"""
enumarate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista)) #[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]


print(lista_enumerada) 
# for numeros in lista_enumerada:
#     print(numeros)