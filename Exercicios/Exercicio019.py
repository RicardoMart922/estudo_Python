# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
catetooposto = float(input('Informe o comprimento do cateto oposto: '))
catetoadjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))