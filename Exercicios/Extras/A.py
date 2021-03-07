for linha in range(5):
    for coluna in range(3):
        if linha == 0 and coluna == 1 or linha == 2 and coluna == 1:
            print('*', end='')
        elif linha == 0 and (coluna == 0 or coluna == 2) or coluna == 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
