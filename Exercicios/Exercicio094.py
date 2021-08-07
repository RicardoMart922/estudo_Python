# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.
dicionarioJogador = dict()
listaGols = list()
dicionarioJogador['nome'] = str(input('Nome do jogador: '))
quantidadePartidas = int(input(f'Quantos partidas {dicionarioJogador["nome"]} jogou? '))
totalGols = 0
for i in range(0, quantidadePartidas):
    gol = int(input(f'Quantos gols na partida {i}: '))
    listaGols.append(gol)
    totalGols += gol
dicionarioJogador['gols'] = listaGols[:]
dicionarioJogador['total'] = totalGols
print('-=' * 30)
print(dicionarioJogador)
print('-=' * 30)
for chave, valor in dicionarioJogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {dicionarioJogador["nome"]} jogou {quantidadePartidas} partidas.')
for i, valor in enumerate(dicionarioJogador['gols']):
    print(f'  => Na partida {i}, fez {valor} gols.')
print(f'Foi um total de {dicionarioJogador["total"]} gols.')
