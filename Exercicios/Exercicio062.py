# Faça um programa que leia um número qualquer e mostre seu fatorial.
numero = int(input('Digite um número: '))
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1 
print('{}! = '.format(numero), end='')
j = 1
k = 1
if numero == 0 or numero == 1:
    print('{}'.format(fatorial))
else:
    while numero >= j:
        if k == 1:
            print('{}'.format(numero), end='')
            k = 2
            numero -= 1
        print(' x {}'.format(numero), end='')
        numero -= 1
    print(' = {}'.format(fatorial))
