# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))
dobro = (2 * numero)
triplo = (3 * numero)
raiz = (numero**(1/2))
print('Dobro = {};\nTriplo = {};\nRaiz Quadrada = {}.'.format(dobro, triplo, raiz)) 