# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
opcao = 0
soma = 0
produto = 0
while opcao != 5:
    print('-=-=-=-=-=-> MENU <-=-=-=-=-=-')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')
    print('-=-' * 10)
    opcao = int(input('Opção: '))
    if opcao == 1:
        soma = (numero1 + numero2)
        print('Somando...')
        sleep(1.5)
        print('A soma de {} com {} é {}'.format(numero1, numero2, soma))
    elif opcao == 2:
        produto = (numero1 * numero2)
        print('Multiplicando...')
        sleep(1.5)
        print('O produto de {} por {} é {}'.format(numero1, numero2, produto))
    elif opcao == 3:
        if numero1 > numero2:
            print('Analisando...')
            sleep(1.5)
            print('O primeiro número é maior que o segundo.')
        elif numero1 == numero2:
            print('Em analise...')
            sleep(1.5)
            print('Os dois números são iguais.')
        else:
            print('Aguarde...')
            sleep(1.5)
            print('O segundo número é maior que o primeiro.')
    elif opcao == 4:
        numero1 = float(input('Informe um número: '))
        numero2 = float(input('Informe outro número: '))
        print('Carregando...')
        sleep(1.5)
    else:
        print('PROCESSANDO...')
        sleep(1.5)
        print('ENCERRADO.')
        