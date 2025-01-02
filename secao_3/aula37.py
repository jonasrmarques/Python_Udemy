"""
Listas em Python
Tipo List - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis:

    append, insert, pop, del, clear, extend, +
    
Create | Read | Update  | Delete
Criar  | Ler  | Alterar | Apagar == lista[i] (CRUD)
"""

lista = [10, 20, 30]
lista.append('Jonas')
nome = lista.pop()
print(lista)

lista.append(1233)
del lista[-1]
# lista.clear()
print(lista)

#insert
lista.insert(0, 5)
print(lista)