"""
Exercício: Calculadora de triângulos
Crie um programa que:

Peça para o usuário digitar três números inteiros positivos (representando os lados de um triângulo).
Verifique se os números formam um triângulo válido:

Um triângulo é válido se a soma de dois lados é sempre maior que o terceiro lado.

Se for um triângulo válido, informe:

Se ele é um triângulo equilátero (todos os lados iguais).
Se ele é um triângulo isósceles (dois lados iguais).
Se ele é um triângulo escaleno (todos os lados diferentes).

Caso não seja válido, exiba uma mensagem dizendo que os lados não formam um triângulo.
"""

lado_a = int(input("Digite um número inteiro para o Lado A: "))
lado_b = int(input("Digite um número inteiro para o Lado B: "))
lado_c = int(input("Digite um número inteiro para o Lado C: "))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    print("É um triangulo válido")
    if lado_a == lado_b == lado_c:
        print("É um triangulo equilatero")
    elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print("É um triangulo isósceles")
    elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
        print("É um triangulo escaleno")
else:
    print("Não forma um triangulo")