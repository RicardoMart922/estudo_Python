# Crie um programa que vai gerar cinco números aleátorios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numero1 = randint(0, 9)
numero2 = randint(0, 9)
numero3 = randint(0, 9)
numero4 = randint(0, 9)
numero5 = randint(0, 9)
maior = numero1
menor = numero1
tupla = (numero1, numero2, numero3, numero4, numero5)
for i in range(0, len(tupla)):
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]
print(f'A tupla: {tupla}')
print(f'O maior elemento da tupla: {maior}')
print(f'O menor elemento da tupla: {menor}')
