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

lista = [10, 20, 30, 40]

# lista[2] = 300
# del lista[2]

# print(lista)
# print(lista[2])

#.append()
lista.append(50)
print(lista)

#.insert()
lista.insert(2, 300)
print(lista)

#.pop()

lista.pop()
print(lista)