# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
qtdnumeros = 0
soma = 0
numero = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    qtdnumeros += 1 
    soma += numero
print('A quntidade de números digitados foi {}'.format(qtdnumeros))
print('A soma de todos os números digitados foi {}'.format(soma)) 
