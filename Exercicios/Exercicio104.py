# Faça um programa que tenha uma função chamada ficha(), que
# receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(n='', g=''):
    if n == '':
        n = '<Desconhecido>'
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
numeroGols = str(input('Número de gols: '))
ficha(nome, numeroGols)
