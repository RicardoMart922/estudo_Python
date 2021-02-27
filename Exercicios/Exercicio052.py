# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
quantidade = 0
for i in range(1, 7):
    numero = int(input('Digite {}º número: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        quantidade += 1
print('Você informou {} números PARES e a soma é {}'.format(quantidade, soma))
