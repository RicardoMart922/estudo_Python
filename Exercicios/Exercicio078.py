# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Cachorro', 'Gato', 'Casa', 'Predio', 'Carro', 'Moto', 'Musica', 'Programador')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
