# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> ...
numero = int(input('Digite um número: '))
fist = 0
second = 1
i = 2
fib = 0
if numero == 0:
    print('Sequência vazia.')
elif numero == 1:
    print('{} -> '.format(fist), end='')
elif numero == 2:
    print('{} -> {} -> '.format(fist, second), end='')
else:
    print('{} -> {} -> '.format(fist, second), end='')
    while i < numero:
        fib = fist + second
        print('{} -> '.format(fib), end='')
        fist = second
        second = fib
        i += 1
print('Fim.')
