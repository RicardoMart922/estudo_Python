def seta(n):
    for i in range(n):
        if i == n - 1:
            print((2 * n) * '*', end='')
            print((i + 1) * '*')
        else:
            print((2 * n) * ' ', end='')
            print((i + 1) * '*')
    for j in range(n - 1, 0, -1):
        print((2 * n) * ' ',end='')
        print(j * '*')
seta(10)
