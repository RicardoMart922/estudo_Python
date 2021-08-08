# Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai
# sortear 5 números e vai colocá-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores PARES sorteados
# pela função anterior.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares é igual a {soma}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
