# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
computador = randint(0, 2)
print('Suas Opções:')
print('[ 0 ] - PEDRA\n[ 1 ] - PAPEL\n[ 2 ] - TESOURA')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('-=-' * 20)
    if computador == 0:
        print('Computador jogou PEDRA.')
    elif computador == 1:
        print('Computador jogou PAPEL.')
    else:
        print('Computador jogou TESOURA.')
    if jogador == 0:
        print('Jogador jogou PEDRA.')
    elif jogador == 1:
        print('Jogador jogou PAPEL.')
    else:
        print('Jogador jogou TESOURA.')
    print('-=-' * 20)
    print('O jogador Venceu!')
elif jogador == computador:
    print('-=-' * 20)
    if jogador == computador == 0:
        print('O Computador jogou PEDRA.')
        print('O Jogador jogou PEDRA.')
    elif jogador == computador == 1:
        print('O Computador jogou PAPEL.')
        print('O Jogador jogou PAPEL.')
    else:
        print('O Computador jogou TESOURA.')
        print('O Jogador jogou TESOURA.')
    print('-=-' * 20)
    print('Empataram!')
else:
    print('-=-' * 20)
    if computador == 0:
        print('Computador jogou PEDRA.')
    elif computador == 1:
        print('Computador jogou PAPEL.')
    else:
        print('Computador jogou TESOURA.')
    if jogador == 0:
        print('Jogador jogou PEDRA.')
    elif jogador == 1:
        print('Jogador jogou PAPEL.')
    else:
        print('Jogador jogou TESOURA.')
    print('-=-' * 20)
    print('O Computador Venceu!')
