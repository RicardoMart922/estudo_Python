# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com uma pausade 1 segundo entre eles.
from time import sleep
print('Contagem regressiva: ')
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('   +   Feliz Ano Novo!   +   ')
print('  +++                   +++  ')
print(' +++++                 +++++ ')
print('+++++++               +++++++')
print(' +++++                 +++++ ')
print('  +++                   +++  ')
print('   +                     +   ')
print('   |                    "|"  ')
print('  "|"                    |   ')
print('   |                    *|*  ')
print('  *|*                    |   ')
print('  888                   888  ')
print('  888                   888  ')