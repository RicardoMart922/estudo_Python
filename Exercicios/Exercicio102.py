# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 18:
        return 'VOTO NEGADO'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


print('-' * 30)
anoNascimento = int(input('Digite o ano que você nasceu: '))
print(voto(anoNascimento))
