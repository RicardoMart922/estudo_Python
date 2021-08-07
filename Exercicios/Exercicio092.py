# Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
dicionarioJogadares = {'Jogador1': randint(1, 6),
                       'Jogador2': randint(1, 6),
                       'Jogador3': randint(1, 6),
                       'Jogador4': randint(1, 6)}
print('Valores sorteados!')
for key, value in dicionarioJogadares.items():
    print(f'   O {key} tirou {value} no dado!')
    sleep(1)

print(' <><> Ranking de Jogadores <><>')
for chave, valor in enumerate(sorted(dicionarioJogadares.items(), key=itemgetter(1), reverse=True)):
    print(f'   {chave+1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)
