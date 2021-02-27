# Faça um progama que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Insira seu peso:(Kg) '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso digitado foi {:.2f} Kg'.format(maior))
print('O menor peso digitado foi {:.2f} Kg'.format(menor))
