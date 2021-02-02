# Operadores aritméticos 
# Soma (+)
# Multiplicação (*)
# Divisão Real (/)
# Divisão inteira (//)
# Exponenciação (**)
# Resto da divisão (%)
# 
# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
soma = (numero1 + numero2)
produto = (numero1 * numero2)
divisaoreal = (numero1 / numero2)
divisaointeira = (numero1 // numero2)
potencia = (numero1**numero2)
restodivisao = (numero1 % numero2)
print('Soma = {};\nProduto = {};\nDivisão Real = {:.3f};\nDivisão Inteira = {};\nPotência = {};\nResto da Divisão = {}.'.format(soma, produto, divisaoreal, divisaointeira, potencia, restodivisao))
