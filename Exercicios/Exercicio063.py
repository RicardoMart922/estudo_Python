# Refaça o desafio 053, lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros termos d progressãousando a estrutura while.
a1 = float(input('Informe o primeiro termo da P.A: '))
razao = int(input('Informe o razão da P.A: '))
elemento = a1
i = 1
print('Os 10 Primeiros Termos')
while i < 11:
    print('{}º Termo = {}'.format(i, elemento))
    elemento += razao
    i += 1
    