# Faça um programa que tenha uma função chamada area(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# área do terreno.
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:5.2f} x{comprimento:5.2f} é de {a:5.2f}m²')


print('> Controle de terrenos <')
print('-=' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
