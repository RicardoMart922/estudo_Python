# faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A";
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer: '))
minuscula = frase.count('a')
maiuscula = frase.count('A')
quantidadeA = (maiuscula + minuscula)
print('A letra "A" ou "a" aparece {} vezes na frase.'.format(quantidadeA))
primeira = frase.find('a')
primeiraA = frase.find('A')
ultima = frase.find('a')
ultimaA = frase.find('A')
