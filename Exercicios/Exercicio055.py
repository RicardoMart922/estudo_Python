# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada não é um PALÍNDROMO.')
    