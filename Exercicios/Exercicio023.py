# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
lista = nome.split()
print('A quantidade de letras do seu nome é {}.'.format(len(lista[0] + lista[1] + lista[2])))
print('A quantidade de letras do seu primeiro nome é {}.'.format(len(lista[0])))
