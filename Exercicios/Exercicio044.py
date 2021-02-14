# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Mostre o tipo de triângulo formado:
# Isóceles - Dois lados iguais;
# Equilátero - Todos os lados iguais;
# Escaleno - Todos os lados diferentes.
lado1 = float(input('1º Lado: '))
lado2 = float(input('2º Lado: '))
lado3 = float(input('3º Lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos informados podem formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('O triângulo formado é do tipo EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo formado é do tipo ISÓCELES.')
    elif lado1 != lado2 != lado3:
        print('O triângulo formado é do tipo ESCALENO.')
else:
    print('Os segmentos informados não podem formar um triângulo.')