"""

split e join com list e str
split - divide uma string
join - une uma string

"""

frase = '   Olha só que,    coisa interessante    '

lista_frasecruas = frase.split(",")


lista_frases = []

for i, frases in enumerate(lista_frasecruas):
    lista_frases.append(lista_frasecruas[i].strip())

print(lista_frasecruas)
print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)
