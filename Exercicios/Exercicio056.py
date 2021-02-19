# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for i in range(1, 8):
    nascimento = int(input('Ano de nascimento: '))
    idade = (atual - nascimento)
    if idade >= 21:
        maiores += 1
    else:
        menores += 1 
print('A quantidade de pessoas que ainda não atingiram a maioridade é {}'.format(menores))
print('A quantidade de pessoas que já atingiram a maioridade é {}'.format(maiores))
    