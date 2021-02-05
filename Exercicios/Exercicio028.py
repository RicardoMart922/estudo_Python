# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: '))
lista = nome.split()
ultimo = int(len(lista))
print('Primeiro: {}'.format(lista[0]))
print('Último: {}'.format(lista[ultimo-1]))