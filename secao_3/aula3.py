"""
Python = Linguagem de Programação
Tipo de tipagem = Dinâmica / Forte 
|| Dinâmica: Já sabe qual o tipo da informação que ta indo pra ele 
|| Forte: Não permite a conversão entre tipos de dados diferentes
||___________________________________________________________________________________
->  x = 10                                                                          |
    s = "Texto"                                                                     |
    s = x  # Erro de tipo se tentarmos concatenar diretamente tipos incompatíveis   |
____________________________________________________________________________________|

str -> string -> texto
Strings são textos que estão dentro de aspas    
"""


# Aspas simples
print('Jonas Rafael')
print(1, 'Jonas "Rafael"')

# Aspas duplas
print("Olá mundo")
print(2, "Olá 'mundo'")

# Escape
print("Olá \"mundo\"") #\ e o caractere é o caractre de escape, significa que o caracter que tiver após a barra invertida será pulado e não será interpretado

# r

print(r"Olá \"mundo\"")  # O r faz com que o caracter de escape apareça