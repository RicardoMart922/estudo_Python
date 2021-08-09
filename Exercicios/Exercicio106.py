# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - A situação(opcional).
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    => Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dictnotas = dict()
    dictnotas['total'] = len(n)
    dictnotas['maior'] = max(n)
    dictnotas['menor'] = min(n)
    dictnotas['média'] = sum(n) / len(n)

    if sit:
        media = dictnotas['média']
        if 7.5 < media <= 10:
            dictnotas['situação'] = 'Boa'
        elif 5.5 < media <= 7.5:
            dictnotas['situação'] = 'Razoável'
        elif media <= 5.5:
            dictnotas['situação'] = 'Ruim'
    return dictnotas


dnotas = notas(6, 8, 7.7, 3, sit=True)
print(dnotas)
help(notas)
