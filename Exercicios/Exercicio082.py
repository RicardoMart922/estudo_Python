# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados;
# B) A lista de valores, ordenada de forma decrescente;
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break
lista.sort(reverse=True)
print(f'Lista: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
