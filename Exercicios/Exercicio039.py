# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.
numero = int(input('Digite um número qualquer: '))
print('''Escolha uma das bases para a conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')