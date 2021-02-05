# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
ocorrencia = 'SILVA' in nome.upper()
print('Seu nome tem Silva? {}'.format(ocorrencia))