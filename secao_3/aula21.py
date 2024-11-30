"""
    Interpolação básica de strings
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal(ABCDEF0123456789)
    
"""

nome = "Jonas" #String
preco = 1000.9589768 #Float
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print("O hexa de %d é %04x" % (15, 15))

