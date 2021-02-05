# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80.00:
    multa = 7.00 * (velocidade - 80)
    print('Você foi multado.')
    print('O valor da multa é R${:.2f}'.format(multa))
else:
    print('Você não foi multado.')