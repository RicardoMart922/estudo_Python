# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
jogada = 0
escolha = ''
soma = 0
cont = 0
print('-=-' * 12)
print('#' * 10,' PAR ou IMPAR ', '#' * 10)
while True:
    computador = randint(0, 10)
    print('-=-' * 12)
    jogada = int(input('Sua jogada: '))
    print('-=-' * 12)
    while True:
        escolha = str(input('Você quer PAR ou IMPAR? ')).upper()
        print('-=-' * 12)
        if escolha == 'PAR' or escolha == 'IMPAR':
            break
    soma = (computador + jogada)
    if escolha == 'PAR' and soma % 2 == 0:
        cont += 1
        print('Você venceu! Parabéns!!!')
        print(f'Sua jogada foi {jogada} e a do computador foi {computador}.')
        print(f'A soma das jogadas foi {soma}.')
    elif escolha == 'IMPAR' and soma % 2 != 0:
        cont += 1
        print('Você venceu! Parabéns!!!')
        print(f'Sua jogada foi {jogada} e a do computador foi {computador}.')
        print(f'A soma das jogadas foi {soma}.')
    elif escolha == 'PAR' and soma % 2 != 0:
        print('Você perdeu!!!')
        print(f'Sua jogada foi {jogada} e a do computador foi {computador}.')
        print(f'A soma das jogadas foi {soma}.')
        break
    elif escolha == 'IMPAR' and soma % 2 == 0:
        print('Você perdeu!!!')
        print(f'Sua jogada foi {jogada} e a do computador foi {computador}.')
        print(f'A soma das jogadas foi {soma}.')
        break
if cont > 1:
    print(f'Você Ganhou {cont} vezes.')
elif cont == 0:
    print('Você não ganhou nenhuma vez.')
elif cont == 1:
    print('Você Ganhou uma vez.')
