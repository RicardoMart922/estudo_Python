# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
distancia = float(input('Informe a distância da viagem em Km: '))
if distancia <= 200.00:
    preco = (distancia * 0.50)
    print('O preço da passagem é R${:.2f}'.format(preco))
else:
    preco = (distancia * 0.45)
    print('O preço da passagem é R${:.2f}'.format(preco))