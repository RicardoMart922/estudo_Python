for linha in range(5):
    for coluna in range(3):
        if (linha == 0 and coluna == 0) or (linha == 4 and coluna == 0):
            print(' ', end='')
        elif linha == 0 or linha == 4 or coluna == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
