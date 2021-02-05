# Estrutura condicional
# if condição
#   bloco de código
# else:
#   bloco de código
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1 + nota2)/2.0)
print('Sua média foi {:.2f}'.format(media))
if media < 6:
    print('Você estar Reprovado!')
else:
    print('Você estar Aprovado!')