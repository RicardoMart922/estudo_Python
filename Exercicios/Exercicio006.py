# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('Digite um número inteiro: '))
antecessor = (numero-1)
sucessor = (numero+1)
print('O \033[4mantecessor\033[m de {} é {}.\nO \033[4msucessor\033[m de {} é {}.'.format(numero, antecessor, numero, sucessor))