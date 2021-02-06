# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número {} é \033[1;34mPar\033[m.'.format(numero))
else:
    print('O número {} é \033[1;34mÍmpar\033[m.'.format(numero))