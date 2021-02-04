# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Informe o valor do ângulo: '))
print('Seno = {}\nCosseno = {}\nTangente = {}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))