numero = int(input("Digite o número da fatorial"))

resultado = 1

if numero == 0:
    resultado = 1
else:
    for i in range(1, numero + 1):
        resultado *= i

print(f"O fatorial de {numero} é {resultado}")