# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('\033[4;31mUnidade\033[m: {}'.format(unidade))
print('\033[4;32mDezena\033[m: {}'.format(dezena))
print('\033[4;33mCentena\033[m: {}'.format(centena))
print('\033[4;34mMilhar\033[m: {}'.format(milhar))
