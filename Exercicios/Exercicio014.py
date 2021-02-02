# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o salário do funcionário: R$ '))
novosalario = (salario + (salario*0.15))
print('O novo salário é R$ {:.2f}'.format(novosalario))