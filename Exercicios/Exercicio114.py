# Reescreva a função leiaInt() que fizemos no desafio 105, incluindo agora a possibilidade da digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.
def leiaInt(text):
    while True:
        try:
            numero = int(input(text))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Por favor, digite um número inteiro válido!\033[m')
            continue
        else:
            return numero


def leiaFloat(text):
    while True:
        try:
            numero = float(input(text))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Por favor, digite um número real válido!\033[m')
            continue
        else:
            return numero


n1 = leiaInt('Número inteiro: ')
n2 = leiaFloat('Número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
