"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
   
Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    O resultado é o valor da conta
    
o primeiro dígito do CPF é 7
"""

# cpf = "713.299.250-33"
# cpf_sem_caracteres = cpf.replace(".", "").replace("-", "")
# cpf_usual = cpf_sem_caracteres[:9]
# print(cpf_usual)

# somado = 0

# multiplicado = 0

# resto = 0

# contador = 10

# laco = True

# indice = 0

# resultado = 0

# while True:
    
#     while contador >= 2:
#         # print(int(cpf_usual[indice]))
#         multiplicado += int(cpf_usual[indice]) * contador
#         indice+=1
#         contador -= 1
        
#     multiplicado = multiplicado * 10
#     resto = multiplicado % 11
    
#     if resto > 9:
#         resultado = 0
#     else:
#         resultado = resto

#     print(f"O primeiro digito do CPF é: {resultado}")
        
#     break




#Ou#

"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
   
Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    O resultado é o valor da conta
    
o primeiro dígito do CPF é 7
"""


cpf = "713.299.250-33"
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
print(f"O seu primeiro dígito é {primeiro_digito}")
    
