# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))
area = (largura*altura)
quantidadetinta = area/2.0
print('A área da parede é {} m².'.format(area))
print('A quantidade de tinta necessaria para pintar a parede é de {} litros'.format(quantidadetinta))