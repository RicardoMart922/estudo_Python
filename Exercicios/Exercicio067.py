# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
numero = 0
totalnumeros = 0
soma = 0
maior = 0
menor = 0
resposta = ''
while resposta != 'N':
    numero = int(input('Digite um número: '))
    totalnumeros += 1
    soma += numero
    if totalnumeros == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = str(input('Você quer continuar a digitar números [S/N]? ')).upper()
print('A média entre todos os {} números digitados é {:.2f}'.format(totalnumeros, (soma/totalnumeros)))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
