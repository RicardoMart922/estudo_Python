# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero = randint(0, 5)
print('== Tente descobrir que número o computador pesou! ==')
chute = int(input('Digite um número entre 0 e 5: '))
print('O número é {}'.format(numero))
if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print('Infelizmente, você errou!')