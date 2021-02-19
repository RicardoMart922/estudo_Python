# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.
media = 0
nomemasc = ''
velho = 0
qtdmulheres = 0
interadorM = 0
interadorF = 0
for i in range(1, 5):
    print('----- {}º PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))
    media += idade
    if i == 1 and sexo in 'MASCULINOmasculinoMasculinoMm':
        velho = idade
        nomemasc = nome
        interadorM += 1
    if sexo in 'MASCULINOmasculinoMasculinoMm' and idade > velho:
        velho = idade
        nomemasc = nome
    if sexo in 'FEMININOfemininoFemininoFf' and idade < 20:
        interadorF += 1
        qtdmulheres += 1
print('A média de idade do grupo é {:.1f}'.format(media / 4.0))
if interadorM != 0:
    print('O nome do homem mais velho é {}'.format(nomemasc))
else:
    print('Não há nenhum homem nesse grupo.')
if sexo in 'FEMININOfemininoFemininoFf' and interadorF != 0: 
    print('A quantidade de mulheres com menos de 20 anos é {}'.format(qtdmulheres))
else:
    print('Não há nenhuma mulher nesse grupo.')