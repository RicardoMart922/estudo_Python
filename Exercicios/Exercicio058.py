# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.
nome = ''
idade = 0
sexo = ''
media = 0
nomemasc = ''
interador = 0
velho = 0
qtdfeminino = 0
for i in range(1, 5):
    nome = str(input('Informe seu nome: '))
    sexo = str(input('Informe seu sexo: '))
    idade = int(input('Informe sua idade: '))
    media += idade
    if sexo == 'MASCULINO' or sexo == 'masculino' or sexo == 'Masculino':
        interador += 1
        if interador == 1 :
            velho = idade
        else:
            if idade > velho:
                velho = idade
                nomemasc = nome
    if sexo == 'FEMININO' or sexo == 'feminino' or sexo == 'Feminino' and idade < 20:
        qtdfeminino += 1
print('A média de idade do grupo é {:.2f}'.format(media / 4.0))
if interador != 0:
    print('O nome do homem mais velho é {}'.format(nomemasc))
else:
    print('Não há nenhum homem nesse grupo.')
if sexo == 'FEMININO' or sexo == 'feminino' or sexo == 'Feminino': 
    print('A quantidade de mulheres com menos de 20 anos é {}'.format(qtdfeminino))
else:
    print('Não há nenhuma mulher nesse grupo.')