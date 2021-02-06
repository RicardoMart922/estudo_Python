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
print('Soma = \033[32m{}\033[m;\nProduto = \033[33m{}\033[m;\nDivisão Real = \033[34m{:.3f}\033[m;\nDivisão Inteira = \033[35m{}\033[m;\nPotência = \033[36m{}\033[m;\nResto da Divisão = \033[31m{}\033[m.'.format(soma, produto, divisaoreal, divisaointeira, potencia, restodivisao))
