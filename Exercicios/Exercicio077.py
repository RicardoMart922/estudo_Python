# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = ('Lápis', 0.65, 'Caneta', 0.75, 'Caderno', 13.50, 'Mochila', 26.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R$ {tupla[pos]:>7.2f}')
print('-'*40)
