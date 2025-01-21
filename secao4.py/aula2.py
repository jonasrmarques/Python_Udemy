"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebem apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f"{x=} y={y}", "|", "x + y = ", x + y)
    

soma(10, 10, 3)
soma(y=10, z=4, x=5)