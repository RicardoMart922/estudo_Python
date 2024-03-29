# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.
from time import sleep


def maior(*valores):
    cont = m = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'Foram inseridos {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior(0)
