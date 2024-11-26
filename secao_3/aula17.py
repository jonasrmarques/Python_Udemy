# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 | 0.0 | '' | False
# Também existe o tipo none que é usado para representar um não valor

entrada = input("[E]ntrar [S]air: ").upper()
senha = input('Senha: ')

validado = '123456'

if entrada == 'E' and senha == validado:
    print('Entrar')
else:
    print('Sair')


print(True and True)
print(True and True and True)
print(True and False)
print(True and True and False)
print(False and False)
print(False and False and True)