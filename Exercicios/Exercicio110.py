# Modifique as funções que foram criadas no desafio 108 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from Exercicio112.utilidades import moeda
p = float(input('Digite o preço: R$'))
print(f'A métade do {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro do {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumetar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
