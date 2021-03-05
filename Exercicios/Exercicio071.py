# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
opcao = ''
nome = ''
preco = 0
gasto = 0
i = 0
while(True):
    nome = str(input('Nome: '))
    gasto += preco
    if preco < 1000:
        i += 1 
    preco = float(input('Preço: '))
    
    opcao = str(input('Quer continuar [S/N]: ')).upper()
    if opcao == 'N':
        break
    
