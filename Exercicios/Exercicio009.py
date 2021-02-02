# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor em metros: '))
centimetros = (valor * 100)
milimetros = (valor * 1000)
print('{} metros = {} centímetros;\n{} metros = {} milímetros.'.format(valor, centimetros, valor, milimetros))