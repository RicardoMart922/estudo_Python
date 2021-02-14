# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantas anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Informe o preço da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Informe em quantos anos você pretende pagar: '))
prestacao = (casa / (anos * 12))
minimo = (salario * 0.3)
print('Para pagar a casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
