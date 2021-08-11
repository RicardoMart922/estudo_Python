def leiaInt(text):
    while True:
        try:
            numero = int(input(text))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Por favor, digite um número inteiro válido!\033[m')
            continue
        else:
            return numero


def linha(tam=42):
    return '-' * tam


def cabecalho(text):
    print(linha())
    print(text.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'\033[0;33m{cont}\033[m - \033[0;34m{item}\033[m')
        cont += 1
    print(linha())
    opcao = leiaInt('\033[0;32mSua opção\033[m: ')
    return opcao



