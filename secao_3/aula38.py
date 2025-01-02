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

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)