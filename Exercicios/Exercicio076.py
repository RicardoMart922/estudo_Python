# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares
tupla = (int(input('Digite o 1º número: ')), 
        int(input('Digite o 2º número: ')), 
        int(input('Digite o 3º número: ')), 
        int(input('Digite o 4º número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição.')
print(f'O valores pares são: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
