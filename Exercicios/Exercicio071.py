# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
opcao = ''
nome = ''
nomeprodutobarato = ''
preco = 0
totgasto = 0
menorpreco = 0
i = 0
while(True):
    nome = str(input('Nome: '))
    preco = float(input('Preço: '))
    if preco < menorpreco:
        menorpreco = preco
        nomeprodutobarato = nome
    totgasto += preco
    menorpreco = preco
    if preco > 1000:
        i += 1 
    opcao = str(input('Quer continuar [S/N]: ')).upper()
    if opcao == 'N':
        break
print(f'O total gasto na compra foi R${totgasto:.2f}')
if i == 0:
    print('Nenhum produto custa mais de R$1000,00.')
if i == 1:
    print('Apenas 1 produto custam mais de R$1000,00.')
else:
    print(f'{i} produtos custam mais de R$1000,00.')
print('O nome do produto mais barato é {}.'.format(nomeprodutobarato))
