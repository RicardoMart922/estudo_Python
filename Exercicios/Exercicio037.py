# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos informados podem formar um triângulo!')
else:
    print('Os segmentos informados não podem formar um triângulo!')
