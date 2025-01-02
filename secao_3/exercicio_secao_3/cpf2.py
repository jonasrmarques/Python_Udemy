"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

cpf = "128.754.204-29"
cpf_sem_caracteres = cpf.replace(".", "").replace("-", "")
cpf_usual = cpf_sem_caracteres[:9]

contador = 10

multiplicacao = 0

for numero in cpf_usual:
    multiplicacao += int(numero) * contador
    contador-=1
    
resultado = multiplicacao * 10 % 11

primeiro_digito = 0

if resultado > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado

print(f"Seu primeiro dígito é: {primeiro_digito}")


cpf_segundo_digito = cpf_usual + str(primeiro_digito)


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


cpf_validado = f"{cpf_usual}{primeiro_digito}{segundo_digito}"
print(cpf_validado)

if cpf_sem_caracteres == cpf_validado:
    print("Seu cpf é válido")
else:
    print("Seu cpf é inválido")