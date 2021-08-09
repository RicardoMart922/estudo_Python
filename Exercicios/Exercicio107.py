# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando
# o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.
c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[0;30m',      # 6 - Branco
    )


def sitema():
    from time import sleep
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 4)
        resp = str(input('Função ou Biblioteca >>> '))
        if resp.upper() == 'FIM':
            titulo('Finalizando', 5)
            break

        sleep(0.3)
        titulo(f'Acessando o manual do comando {resp}', 3)
        sleep(1)
        print(c[5], end='')
        help(resp)
        print(c[0], end='')


def titulo(mensagem, cor=0):
    tam = len(mensagem)+4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {mensagem}')
    print('~' * tam)
    print(c[0], end='')


sitema()
