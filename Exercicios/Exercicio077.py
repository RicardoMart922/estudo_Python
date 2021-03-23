# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = ('Lápis', 0.65, 'Caneta', 0.75, 'Caderno', 13.50, 'Mochila', 26.00)
p = 0
s = 1
for i in range(0, 8):
    print(f'{tupla[p]} ....... R${tupla[s]}')
    p = p + 2
    s = s + 2
print('Fim.')
