# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maisdezoito = 0
qtdmulheres = 0
qtdhomens = 0
idade = 0
opcao = ''
sexo = ''
print('-= Informe a idade e o sexo para o cadastro =-')
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maisdezoito += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                qtdhomens += 1
            if sexo == 'F' and idade < 20:
                qtdmulheres += 1
            break
    while True:
        opcao = str(input('Quer continuar [S/N]: ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
if maisdezoito == 0:
    print('Nenhuma pessoa com mais de 18 anos foi cadastrada.')
elif maisdezoito == 1:
    print('Foi cadastrado uma pessoa com mais de 18 anos.')
else:
    print(f'Foi cadastrado {maisdezoito} pessoas com mais de 18 anos.')
if qtdhomens == 0:
    print('Nenhum homem foi cadastrado.')
elif qtdhomens == 1:
    print('Apenas um homem foi cadastrado.')
else:
    print(f'A quantidade de homens cadastrados foi {qtdhomens}.')
if qtdmulheres == 0:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada.')
elif qtdmulheres == 1:
    print('Apenas uma mulher com menos de 20 anos foi cadastrada.')
else:
    print(f'A quantidade de mulheres com menos de 20 anos que foram cadastradas foi {qtdmulheres}.')
    