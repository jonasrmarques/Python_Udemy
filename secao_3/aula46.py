#Desempacotamento em chamadas
#de métodos e funções

string = "ABCD"
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python','é', 'Legal')

# a, b, *_ , u= lista
# print(a, u)

print(*lista)
print(*string)
print(*tupla)