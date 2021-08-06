# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
# em uma lista composta.
from random import randint
from time import sleep
listaJogos = list()
lista = list()
print('-=' * 16)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-=' * 16)
quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {quantidadeJogos} JOGOS -=-=-=')
numero = 0
for cont1 in range(0, quantidadeJogos):
    for cont2 in range(0, 6):
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
        else:
            while True:
                numero = randint(1, 60)
                if numero not in lista:
                    lista.append(numero)
                    break
    listaJogos.append(lista[:])
    lista.clear()
sleep(1)
for indice in range(0, quantidadeJogos):
    listaJogos[indice].sort()
    print(f'Jogo {indice+1}: {listaJogos[indice]}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
