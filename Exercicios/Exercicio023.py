# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúscula é {}'.format(nome.upper()))
print('Seu nome com letras minúscula é {}'.format(nome.lower()))
print('A quantidade de letras do seu nome é {}.'.format(len(nome) - nome.count(' ')))
print('A quantidade de letras do seu primeiro nome é {}.'.format(nome.find(' ')))
