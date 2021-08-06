# Crie um programa que vai gerar cinco números aleátorios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior = tupla[0]
menor = tupla[0]
for i in range(0, len(tupla)):
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]
print(f'A tupla: ', end=' ')
for cont in range(0, len(tupla)):
    print(tupla[cont], end=' ')
print(f'\nO maior elemento da tupla: {maior}')
print(f'O menor elemento da tupla: {menor}')
