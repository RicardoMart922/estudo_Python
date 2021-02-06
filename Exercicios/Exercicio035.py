# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = float(input('Primeiro valor: '))
numero2 = float(input('Segundo valor: '))
numero3 = float(input('Terceiro valor: '))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('O menor número digitado foi {:.2f}'.format(menor))
print('O maior número digitado foi {:.2f}'.format(maior))