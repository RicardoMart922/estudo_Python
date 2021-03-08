for linha in range(0, 7):
    for coluna in range(0, 7):
        if (((coluna == 1 or coluna == 5) and linha != 6) or (linha == 6 and coluna > 1 and coluna < 5)):
            print('*', end='')
        else:
            print(' ', end='')
    print()
    