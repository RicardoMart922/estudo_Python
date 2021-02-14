# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.
preco = float(input('Informe o preço do produto: R$'))
print('-=-'*20)
print('-=-'*6+'  Formas de Pagamentos  '+'-=-'*6)
print('-=-'*20)
print('Insira o código correspondente com sua escolha:')
print('[1] - À Vista Dinheiro/Cheque;')
print('[2] - À Vista no Cartão;')
print('[3] - Em até 2X no Cartão;')
print('[4] - Em até 3X ou mais no Cartão.')
print('-=-'*20)
opcao = int(input('Sua escolha: '))
if opcao == 1:
    valor = (preco - (preco * 0.1))
    print('O preço do produto será R${:.2f}'.format(valor))
elif opcao == 2:
    valor = (preco - (preco * 0.05))
    print('O novo preço do produto é R${:.2f}'.format(valor))
elif opcao == 3:
    print('O preço do produto é R${:.2f}'.format(preco))
elif opcao == 4:
    valor = (preco + (preco * 0.2))
    print('O preço do produto é R${:.2f}'.format(valor))
else:
    print('Opção inválida!')