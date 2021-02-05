# faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A";
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer: '))
minuscula = frase.count('a')
maiuscula = frase.count('A')
quantidadeA = (maiuscula + minuscula)
frase.find('a')
frase.find('A')
print(quantidadeA)
