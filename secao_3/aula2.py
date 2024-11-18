# \r\n -> CRLF
# \N -> LF

print(12, 34) #É utilizada para exibir informações na tela, ela recebe argumentos
print(56, 78, 1011, sep='-', end='\r\n')
print(56, 78, sep="/", end='##\n') #Esse sep serve para alterar o separador dos argumentos não nomeados
print(910, 1112, sep="/", end='\n') #Esse sep serve para alterar o separador dos argumentos não nomeados
