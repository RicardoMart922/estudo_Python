# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico.
# EX.: n = leiaInt('Digite um n')

def leiaInt(text):
    while True:
        numero = input(text)
        if numero.isnumeric():
            numero = int(numero)
            break
        elif numero.isalpha() or type(numero) != int:
            print('\033[0;31mErro! Digite um número válido.\033[m')

    return numero


n = leiaInt('Digite um n: ')
print(f'O número digitado foi {n}')
