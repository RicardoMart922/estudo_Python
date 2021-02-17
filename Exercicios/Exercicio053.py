# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = float(input('Informe o primeiro termo da P.A: '))
razao = int(input('Informe o razão da P.A: '))
elemento = a1
print('Os 10 Primeiros Termos')
for i in range(1, 11):
    print('{}º Termo = {}'.format(i, elemento))
    elemento += razao