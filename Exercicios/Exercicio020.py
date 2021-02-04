# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Informe o valor do ângulo: '))
print('Seno = {:.2f}'.format(sin(radians(angulo))))
print('Cosseno = {:.2f}'.format(cos(radians(angulo))))
print('Tangente = {:.2f}'.format(tan(radians(angulo))))