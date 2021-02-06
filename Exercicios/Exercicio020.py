# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Informe o valor do ângulo: '))
print('\033[31mSeno\033[m = {:.2f}'.format(sin(radians(angulo))))
print('\033[32mCosseno\033[m = {:.2f}'.format(cos(radians(angulo))))
print('\033[33mTangente\033[m = {:.2f}'.format(tan(radians(angulo))))