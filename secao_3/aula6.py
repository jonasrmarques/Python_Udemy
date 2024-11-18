"""
Conversão de tipos, coerção
type convertion, typecasting, coercion
É o ato de converter um tipo em outro

tipos imutaveis e primitivos:
str, int, float, bool    
"""
print(1 + 1)
print(int('1') + 1)
print('1' + str(1))
print('a' + 'b')
print(bool('')) #String vazia == False
print(bool(' ')) #String com algo até um espaço == True
print(bool(0)) #0 é false
print(bool(1)) #1 é true
print(bool(2)) # 2 é true
print(bool(-2)) # -2 é true
print(bool(0.1)) # 0.1 é true
print(bool(0.0)) # 0.0 é False

#int(), float(), str(), bool() irá mudar o tipo do que tiver dentro