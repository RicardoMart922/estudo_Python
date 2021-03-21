# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))
numero4 = int(input('Digite o 4º número: '))
tupla = (numero1, numero2, numero3, numero4)
par = 0
qtd = 0
pos = 0
for cont in range(0, len(tupla)):
    if tupla[cont] == 9:
        qtd += 1 
for p in range(0, len(tupla)):
    if tupla[p] == 3:
        pos = p
        break
if qtd == 1:
    print(f'O número 9 apareceu {qtd} vez.')
else:
    print(f'O número 9 apareceu {qtd} vezes.')
print(f'O 1º número três apareceu na posição {pos+1}')
print(f'Os números pares da tupla são: ')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        par = tupla[i]
        print(f'{par}, ', end='')
    
