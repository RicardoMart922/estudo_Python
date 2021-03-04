# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o  caixa possui cédulas de R$50, R$20, R$10 e R$1. 
valor = int(input('Qual o valor a ser sacado? R$'))
cinquenta = 0
vinte = 0
dez = 0
um = 0
if valor >= 50:
    while valor >= 50:
        cinquenta += 1
        valor -= 50
if valor >= 20:
    while valor >= 20:
       vinte += 1
       valor -= 20
if valor >= 10:
    while valor >= 10:
        dez += 1
        valor -= 10
if valor >= 1:
    while valor >= 1:
        um += 1
        valor -= 1
print(f'A quantidade de cédulas de R$50,00 é {cinquenta}')
print(f'A quantidade de cédulas de R$20,00 é {vinte}')
print(f'A quantidade de cédulas de R$10,00 é {dez}')
print(f'A quantidade de cédulas de R$1,00 é {um}')