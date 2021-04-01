# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Cachorro', 'Gato', 'Casa', 'Predio', 'Carro', 'Moto', 'Musica')
for i in tupla:
    print(f'\nNa palavra {i} temos ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')
