# Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
from math import trunc
numero = float(input('Digite um número: '))
print('A parte inteira é {}'.format(trunc(numero)))