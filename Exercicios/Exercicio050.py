# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
quantidade = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        quantidade += 1 
print('A soma de todos os {} números ímpares e múltiplos de 3 no intervalo de 1 até 500, foi {}'.format(quantidade, soma))
