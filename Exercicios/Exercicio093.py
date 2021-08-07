# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
import datetime
dicionarioFuncionario = dict()
dicionarioFuncionario['nome'] = str(input('Nome: '))
anoAtual = datetime.date.today().year
anoNascimento = int(input('Ano de nascimento: '))
dicionarioFuncionario['idade'] = anoAtual - anoNascimento
dicionarioFuncionario['ctps'] = int(input('Carteira de trabalho (Digite 0 caso não tenha): '))
if dicionarioFuncionario['ctps'] == 0:
    print('-=' * 30)
    for chave, valor in dicionarioFuncionario.items():
        print(f'  {chave} tem valor {valor}')
elif dicionarioFuncionario['ctps'] > 0:
    dicionarioFuncionario['anoContratacao'] = int(input('Ano de contratação: '))
    dicionarioFuncionario['salario'] = float(input('Salário: R$'))
    dicionarioFuncionario['Aposentadoria'] = dicionarioFuncionario['idade'] + ((dicionarioFuncionario['anoContratacao'] + 35) - anoAtual)
    print('-=' * 30)
    for chave, valor in dicionarioFuncionario.items():
        print(f'  {chave} tem valor {valor}')
else:
    print('Informação inválida!')
