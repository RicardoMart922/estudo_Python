# Aprimore o desafio 094 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.
listaPrincipal = list()
dicionarioJogador = dict()
listaGols = list()
while True:
    dicionarioJogador.clear()
    dicionarioJogador['nome'] = str(input('Nome do jogador: '))
    quantidadePartidas = int(input(f'Quantos partidas {dicionarioJogador["nome"]} jogou? '))

    totalGols = 0
    for i in range(0, quantidadePartidas):
        gol = int(input(f'  Quantos gols na partida {i}: '))
        listaGols.append(gol)
        totalGols += gol
    dicionarioJogador['gols'] = listaGols[:]
    dicionarioJogador['total'] = totalGols

    listaGols.clear()
    listaPrincipal.append(dicionarioJogador.copy())

    while True:
        opcao = str(input('Quer continuar[S/N]? ')).upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Dado inválido.')
    if opcao == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dicionarioJogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(listaPrincipal):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(listaPrincipal):
        print(f'Erro! Não há jogador com o código {busca}.')
    else:
        print(f' --- LEVAMTAMENTO DO JOGADOR {listaPrincipal[busca]["nome"]}')
        for indice, gol in enumerate(listaPrincipal[busca]['gols']):
            print(f'  Na jogo {indice} fez {gol} gols.')
    print('-' * 40)
print('Finalizando por aqui...')
