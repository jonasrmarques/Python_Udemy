"""
Introdução ao desempacotamento + tuplas
"""

nomes = ['Jonas', 'Rafael', 'Marques']


nome1, nome2, nome3 = nomes

print(nome1)

carro1, *_ = ["Fiat", "Sandero", "BMW"]
print(carro1)