import random


nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))
    
print(nove_digitos)

contador = 10

multiplicacao = 0

for numero in nove_digitos:
    multiplicacao += int(numero) * contador
    contador-=1
    
resultado = multiplicacao * 10 % 11

primeiro_digito = 0

if resultado > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado

print(f"Seu primeiro dígito é: {primeiro_digito}")


cpf_segundo_digito = nove_digitos + str(primeiro_digito)


contador = 11
multiplicacao_segundo_digito = 0

for numero in cpf_segundo_digito:
    
    multiplicacao_segundo_digito += int(numero) * contador
    
    contador -= 1

resultado2 = multiplicacao_segundo_digito * 10 % 11

segundo_digito = 0

if resultado2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado2
     
print(f"Seu segundo digito é: {segundo_digito}")


cpf_validado = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
print(cpf_validado)

