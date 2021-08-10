def leiaDinheiro(mensagem, end='\n'):
    valido = False
    while not valido:
        valor = str(input(mensagem)).replace(',', '.').strip()
        if valor.isalpha() and valor == '':
            print(f'\033[0;31mErro! {valor} é inválido.\033[m')
        else:
            valido = True
            return float(valor)


def leiaInt(text):
    while True:
        numero = input(text)
        if numero.isnumeric():
            numero = int(numero)
            break
        elif numero.isalpha() or type(numero) != int:
            print('\033[0;31mErro! Digite um número válido.\033[m')
    return numero
