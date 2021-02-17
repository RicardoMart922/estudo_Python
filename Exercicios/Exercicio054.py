# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número inteiro: '))
contador = 0
resto = 0
for i in range(1, numero+1):
    resto = numero % i
    if resto == 0:
        contador += 1
if contador == 2:
    print('O número {} é primo!'.format(numero))
else:
    print('O número {} não é primo!'.format(numero))