"""

Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

"""

var = "abc"

# print(f'{var}')
# print(f'{var: >10}')
# print(f'{var: <10}')
# print(f'{var: ^10}')

# print(f'{1000000.22131242:,.2f}')


# print(f"O hexa de 1500 é {1500:08x}")

print(f"{var!r}")