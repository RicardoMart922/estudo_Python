# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
listaPar = list()
listaImpar = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break
for num in lista:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'Lista completa: {lista}')
print(f'Lista dos números pares: {listaPar}')
print(f'Lista dos números ímpares: {listaImpar}')
