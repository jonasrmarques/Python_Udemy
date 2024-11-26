#Operadores in e not in
#Strings são iteráveis
# 0 1 2 3 4 5
# R A F A E L
#-6-5-4-3-2-1

nome = 'Rafael'

# print(nome[1])
# print(nome[-1])

# print('a' in nome)
# print('v' in nome)
# print('Raf' in nome)
# print(10 * '-')
# print('xyz' not in nome)
# print('ael' not in nome)

nome = input("Digite seu nome")
encontrar = input("Digite o que deseja encontrar")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")