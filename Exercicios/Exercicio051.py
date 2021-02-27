# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um número: '))
print('-='*3+' TABUADA DE {} '.format(numero)+'=-'*3)
for i in range(0, 11):
    print('{} x {:2} = {}'.format(numero, i, i * numero))
    