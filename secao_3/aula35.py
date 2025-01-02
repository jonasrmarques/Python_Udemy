"""
Listas em Python
Tipo List - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE' #5 caracteres (len)

lista = [] #lista vazia
# print(bool(lista)) #falsy
lista = [123, True, "Jonas", 1.2, [1, 2, 3]]

print(lista)

print(lista[2], type(lista[2]))

lista[-3] = 'Rafael'
print(lista[2], type(lista[2]))