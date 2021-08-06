# Crie um programa onde o usuário possa digitar vários valores numériocos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado. Não posso adicionar!')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break
print('=-=' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')
