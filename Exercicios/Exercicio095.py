# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# Quantas pessoas foram cadastradas;
# A média de idade do grupo;
# Uma lista com todas as mulheres;
# Uma lista com todas as pessoas com idade acima de média.
dicionarioPessoa = dict()
listaPrincipal = list()
soma = media = 0
while True:
    dicionarioPessoa['nome'] = str(input('Nome: '))
    while True:
        dicionarioPessoa['sexo'] = str(input('Sexo [F/M}: ')).upper()[0]
        if dicionarioPessoa['sexo'] in 'FM':
            break
        print('ERRO! Tente um valor válido.')
    dicionarioPessoa['idade'] = int(input('Idade: '))
    soma += dicionarioPessoa['idade']
    listaPrincipal.append(dicionarioPessoa.copy())
    dicionarioPessoa.clear()
    while True:
        opcao = str(input('Quer continuar [S/N]? ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Tente um valor válido.')
    if opcao == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(listaPrincipal)} pessoas cadastradas.')
media = soma / len(listaPrincipal)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for item in listaPrincipal:
    if item['sexo'] == 'F':
        print(f'{item["nome"]} ', end='')
print(f'\nD) Lista de pessoas que estão acima da média: ')
for dicionario in listaPrincipal:
    if dicionario['idade'] >= media:
        print('   ', end='')
        for k, v in dicionario.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>< Encerrado ><')