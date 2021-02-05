# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nome = str(input('Digite o nome da cidade: '))
lista = nome.split()
comeco = 'Santo' in lista[0]
print(comeco)
