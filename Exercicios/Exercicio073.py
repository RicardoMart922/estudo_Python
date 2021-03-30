# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vite.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opcao = ''
numero = 0
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Tente novamente.')
        numero = int(input('Digite um número entre 0 e 20: '))
    else:
        print(f'O número digitado foi o {contagem[numero]}')
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
