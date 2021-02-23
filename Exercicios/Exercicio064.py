# Melhore o desafio 063, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
a1 = float(input('Informe o primeiro termo da P.A: '))
razao = int(input('Informe o razão da P.A: '))
elemento = a1
termo = -1
i = 1
j = 10
print('Os 10 Primeiros Termos')
while i < 11:
    print('{}º Termo = {}'.format(i, elemento))
    elemento += razao
    i += 1
print('Você quer mostrar mais alguns termos? [S/N] ')
opcao = str(input('Opção: ')).upper()
if opcao == 'S':
    qtdtermos = int(input('Quantidade de termos: '))
    while qtdtermos != 0:
        while j < qtdtermos:
            print('{}º Termo = {}'.format(i, elemento))
            elemento += razao
            j += 1
        qtdtermos = int(input('Quantidade de termos: '))
else:
    print('Fim!')