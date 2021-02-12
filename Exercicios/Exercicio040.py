# Escreva um programa que leia dois números inteiros e compares-os, mostrando na tela um mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
if numero1 > numero2:
    print('O primeiro valor é maior.')
elif numero2 > numero1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')