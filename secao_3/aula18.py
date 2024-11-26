# Operadores Lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 | 0.0 | '' | False
# Também existe o tipo none que é usado para representar um não valor


# entrada = input("[E]ntrar [S]air: ")
# senha = input('Senha: ')

# validado = '123456'

# if entrada == 'E' or 'e' and senha == validado:
#     print('Entrar')
# else:
#     print('Sair')
    
#Avaliação de curto circuito

print(True or False)
print(0 or False or 0 or 'abc', True)