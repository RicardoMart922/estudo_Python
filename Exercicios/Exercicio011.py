# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# OBS: Considerar 1 dólar = 5.35 reais
valor = float(input('Informe a quantidade de dinheiro em sua carteira: R$'))
dolares = (valor/5.35)
print('A quantidade de dólares que você pode comprar é US${:.2f}'.format(dolares))