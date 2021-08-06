# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.
listaPrincipal = list()
listaSecundaria = list()
listaTerciaria = list()
while True:
    listaSecundaria.append(str(input('Nome: ')))
    listaTerciaria.append(float(input('Nota 1: ')))
    listaTerciaria.append(float(input('Nota 2: ')))

    listaSecundaria.append(listaTerciaria[:])
    listaTerciaria.clear()

    listaPrincipal.append(listaSecundaria[:])
    listaSecundaria.clear()

    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break

print('-=' * 30)
print(f'{"Nº": <5}', end='')
print(f'{"Nome": <10}', end='')
print(f'{"Média": >10}')
print('-' * 30)
for i in range(0, len(listaPrincipal)):
    print(f'{i: <5}', end='')
    print(f'{listaPrincipal[i][0]: <10}', end='')
    print(f'{(listaPrincipal[i][1][0] + listaPrincipal[i][1][1]) / 2: >10.1f}')
print('-' * 30)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        print('Finalizando...')
        print('<<< Volte sempre >>>')
        break
    elif opcao > len(listaPrincipal):
        print('Erro...')
        print('Tente um número válido!')
    else:
        print(f'Notas de {listaPrincipal[opcao][0]} são {listaPrincipal[opcao][1]}')
    print('-' * 30)
