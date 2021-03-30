# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em alfabética.
# D) Em que posição na tabela está o time da Ceará.
tabela = ('Flamengo - RJ', 'Internacional - RS', 'Atlético - MG', 'São Paulo - SP', 'Fluminense - RJ', 'Grêmio - RS', 'Palmeiras - SP', 'Santos - SP', 'Athletico Paranaense - PR', 'Red Bull Bragantino - SP', 'Ceará - CE', 'Corinthians - SP', 'Atlético - GO', 'Bahia - BA', 'Sport - PE', 'Fortaleza - CE', 'Vasco da Gama - RJ', 'Goiás - GO', 'Coritiba - PR', 'Botafogo - RJ')
print(f'A lista de Times: {tabela}') 
print('-=-' * 10)
print(f'Os primeiros 5 colocados:')
for i in range(0, 5):
    print(f'{i+1}º - {tabela[i]}')
print('-=-' * 10)
print(f'Os últimos 4 colocados:')
for j in range(16, len(tabela)):
    print(f'{j+1}º - {tabela[j]}')
print('-=-' * 10)
ordenar = sorted(tabela)
print(f'Ordem alfabética:')
for k in range(0, len(tabela)):
    print(f'{k+1}º - {ordenar[k]}')
print('-=-' * 10)
posicao = 0
for cont in range(0, len(tabela)):
    if 'Ceará - CE' == tabela[cont]:
        posicao = cont+1
        break
print(f'Posição do Ceará: {posicao}º\n')
