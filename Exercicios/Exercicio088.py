# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados;
# A soma dos valores da terceira coluna;
# O maior valor da segunda linha.
listaMatriz = list()
listaLinha = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        listaLinha.append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
    listaMatriz.append(listaLinha[:])
    listaLinha.clear()

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{listaMatriz[linha][coluna]:^5}]', end='')
    print()

somaPares = 0
somaTerceiraColuna = 0
maiorSegundaLinha = listaMatriz[1][0]
for m in range(0, 3):
    for n in range(0, 3):
        print(f'[ {listaMatriz[m][n]} ]', end='')
        if listaMatriz[m][n] % 2 == 0:
            somaPares += listaMatriz[m][n]
        if (m == 0 or m == 1 or m == 2) and n == 2:
            somaTerceiraColuna += listaMatriz[m][2]
        if listaMatriz[1][n] >= maiorSegundaLinha:
            maiorSegundaLinha = listaMatriz[1][n]
    print()
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}')
