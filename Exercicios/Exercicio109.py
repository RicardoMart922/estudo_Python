# Adapte o código do desafio 108, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.
from Exercicio112.utilidades.moeda import moeda
p = float(input('Digite o preço: R$'))
print(f'A métade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumetar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
