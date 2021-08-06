# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
listaPrincipal = [[], []]
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        listaPrincipal[0].append(valor)
    else:
        listaPrincipal[1].append(valor)
listaPrincipal[0].sort()
print(f'Lista de pares: {listaPrincipal[0]}')
listaPrincipal[1].sort()
print(f'Lista de ímpares: {listaPrincipal[1]}')