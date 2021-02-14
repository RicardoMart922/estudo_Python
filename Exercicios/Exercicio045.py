# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade mórbida.
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em m: '))
imc = (peso/(altura**2))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25.0:
    print('Você está com o peso ideal.')
elif imc > 25.0 and imc <= 30.0:
    print('Você está com sobrepeso.')
elif imc > 30.0 and imc <= 40.0:
    print('Você está com obesidade.')
elif imc > 40.0:
    print('Você está com obesidade mórbida.')