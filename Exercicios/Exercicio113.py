# Dentro do paconte utilidades que criamos no desafio 112, temos o módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função input(), mas com uma validação de dados para
# aceitar apenas valores que sejam monetários.
from Exercicio112.utilidades.dado import leiaDinheiro
p = leiaDinheiro('Digite o preço: R$')
print(p)

