# Faça um programa que leia 5 valores numéricos e guarde em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print('=-=' * 20)
print(f'Você digitou os valores {lista}')
maior = max(lista)
print(f'O maior valor digitado foi {maior} na posição ', end='')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}... ', end='')
menor = min(lista)
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}... ', end='')
