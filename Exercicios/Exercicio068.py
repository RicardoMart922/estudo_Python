# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
numero = 0
while 1:
    print('^=^' * 10)
    numero = int(input('Digite um número: '))
    print('^=^' * 10)
    if numero < 0:
        print('Encerrando o programa...')
        break
    print('-=-' * 10)
    print('Tabuada do número {}.'.format(numero))
    print('-=-' * 10)
    print('{} x {:2} = {}'.format(numero, 0, numero*0))
    print('{} x {:2} = {}'.format(numero, 1, numero*1))
    print('{} x {:2} = {}'.format(numero, 2, numero*2))
    print('{} x {:2} = {}'.format(numero, 3, numero*3))
    print('{} x {:2} = {}'.format(numero, 4, numero*4))
    print('{} x {:2} = {}'.format(numero, 5, numero*5))
    print('{} x {:2} = {}'.format(numero, 6, numero*6))
    print('{} x {:2} = {}'.format(numero, 7, numero*7))
    print('{} x {:2} = {}'.format(numero, 8, numero*8))
    print('{} x {:2} = {}'.format(numero, 9, numero*9))
    print('{} x {:2} = {}'.format(numero, 10, numero*10))
    print('-=-' * 10)
