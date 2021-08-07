# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionarioAluno = dict()
dicionarioAluno['nome'] = str(input('Nome: '))
dicionarioAluno['media'] = float(input(f'Média de {dicionarioAluno["nome"]}: '))
if dicionarioAluno['media'] >= 7.0:
    dicionarioAluno['situacao'] = 'Aprovado'
elif 5 <= dicionarioAluno['media'] < 7:
    dicionarioAluno['situacao'] = 'Recuperação'
else:
    dicionarioAluno['situacao'] = 'Reprovado'
print('-=' * 30)
for chave, valor in dicionarioAluno.items():
    print(f'  - {chave} é igual {valor}')
