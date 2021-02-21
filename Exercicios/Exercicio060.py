# Melhore o jogo do desafio 030 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forma necessários para vencer.
from random import randint
from time import sleep
numero = randint(0, 10)
print('-=-' * 20)
print('-=--' * 5,'=-> ADIVINHAÇÃO <-=','--=-' * 5)
print('-=-' * 20)
print('\033[4mComputador\033[m: - Pensei em número, tente adivinhar que número é!\n')
chute = int(input('Digite um número entre 0 e 10: '))
palpites = 1
while chute != numero:
    print('\033[36mPROCESSANDO...\033[m')
    sleep(3)
    print('Você errou. Tente novamente.')
    chute = int(input('Digite um número entre 0 e 10: '))
    palpites += 1
print('Computador: - O número que eu pensei foi {}'.format(numero))
print('\033[1;31mParabéns\033[m! Você acertou!')
if palpites == 1:
    print('Você precisou de {} palpite para vencer o Computador!',format(palpites))
    print('\033[1;31mVocê é demais!\033[m')
else:
    print('Você precisou de {} palpites para vencer o Computador!'.format(palpites))