# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero = randint(0, 5)
print('== Tente descobrir que número o computador pesou! ==')
print('Computador: - Pensei em número, tente adivinhar que número é!')
chute = int(input('Digite um número entre 0 e 5: '))
print('Computador: - O número que eu pensei foi {}'.format(numero))
if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print('Infelizmente, você errou!')