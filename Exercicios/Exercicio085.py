# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas;
# Uma listagem com as pessoas mais pesadas;
# Uma listagem com as pessoas mais leves.
listaPrincipal = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    listaPrincipal.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break
print(f'A quantidade de pessoas cadastradas foi {len(listaPrincipal)}')

maior = listaPrincipal[0][1]
for p in range(0, len(listaPrincipal)):
    if listaPrincipal[p][1] > maior:
        maior = listaPrincipal[p][1]
print(f'O maior peso foi de {maior}. Peso de ', end='')

for p in listaPrincipal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()

menor = listaPrincipal[0][1]
for p in range(0, len(listaPrincipal)):
    if listaPrincipal[p][1] < menor:
        menor = listaPrincipal[p][1]
print(f'O menor peso foi de {menor}. Peso de ', end='')

for p in listaPrincipal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
