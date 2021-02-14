# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ap serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento;
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date
anonascimento = int(input('Informe o ano do seu nascimento: '))
anoatual = date.today().year
idade = (anoatual - anonascimento)
if idade < 18:
    print('Você ainda não está apto para realizar o alistamento no serviço militar.')
    falta = (18 - idade)
    if falta == 1:
        print('Falta {} ano para você poder se alistar.'.format(falta))
    else:
        print('Falta {} anos para você poder se alistar.'.format(falta))
elif idade == 18:
    print('Você está apto para o alistamento militar.')
else:
    print('Você já passou da idade para realizar o alistamento militar.')
    passou = (idade - 18)
    if passou == 1:
        print('Passou {} ano do prazo recomendado.'.format(passou))
    else:
        print('Passou {} ano do prazo recomendado.'.format(passou))