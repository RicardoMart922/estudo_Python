# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.
preco = float(input('Informe o preço do produto: R$'))
print('-=-'*20)
print(6*'-=-'+'  Formas de Pagamentos  '+'-=-'*6)
print('-=-'*20)
print('Insira o código correspondente com sua escolha:')
print('[1] - À Vista Dinheiro/Cheque;')
print('[2] - À Vista no Cartão;')
print('[3] - Em até 2X no Cartão;')
print('[4] - Em até 3X ou mais no Cartão.')
print('-=-'*20)
opcao = int(input('Sua escolha: '))
if opcao == 1:
    juros = (preco * 0.1)
    valor = (preco - juros)
    print('Devido a sua forma de pagamento ser à vista, terá um desconto de R${:.2}'.format(juros))
elif opcao == 2:
    juros = (preco * 0.05)
    valor = (preco - juros)
    print('Devido a sua forma de pagamento ser à vista no cartão, terá um desconto de R${:.2}'.format(juros))
elif opcao == 3:
    parcela = (preco / 2)
    print('Sua compra será parcelada em 2 vezes de R${:.2f}'.format(parcela))
elif opcao == 4:
    vezes = int(input('Em quantas vezes você quer parcelar? '))
    juros = (preco * 0.2)
    valor = (preco + juros)
    parcela = (valor / vezes)
    print('Devido a sua forma de pagamento, terá um acréscimo de R${:.2f} de juros'.format(juros))
    print('Sua compra será parcelada em {} vezes de R${:.2f}'.format(vezes, parcela))
else:
    valor = preco
    print('Opção inválida!')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, valor))