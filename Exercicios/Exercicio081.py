# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = list()
for num in range(0, 5):
    valor = int(input('Digite um valor: '))
    if num == 0:
        lista.append(valor)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < lista[-1]:
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
