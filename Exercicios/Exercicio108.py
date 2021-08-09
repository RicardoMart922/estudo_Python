# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use algumas
# dessas funções.
from Exercicio112.utilidades import moeda
p = float(input('Digite o preço: R$'))
print(f'A métade do {p} é {moeda.metade(p)}')
print(f'O dobro do {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumetar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
