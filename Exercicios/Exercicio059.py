# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [S/M]: ')).upper()
while sexo != 'F' and sexo != 'M':
    print('Informação inválida. Tente novamente.')
    sexo = str(input('Informe seu sexo [S/M]: ')).upper()
print('Informação válida.')
