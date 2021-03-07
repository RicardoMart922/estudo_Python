for linha in range(7):
    for coluna in range(5):
        if coluna == 0:
            print('*', end='')
        elif (linha == 0 or linha == 3) and (coluna > 0 and coluna < 4):
            print('*', end='')
        elif (coluna == 4) and (linha != 0 and linha != 3):
            print('*', end='')
        else:
            print(end=' ')
    print()
