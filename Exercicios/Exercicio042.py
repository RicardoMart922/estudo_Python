# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO;
# Média entre 5.0 e 6.9: RECUPERAÇÃo;
# Média 7.0 ou superior: APROVADO.
nota1 = float(input('1º NOTA: '))
nota2 = float(input('2º NOTA: '))
media = ((nota1 + nota2) / 2.0)
print('Sua média foi {:.2f}'.format(media))
if media < 5.0:
    print('Voçê está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('Voçê está RECUPERAÇÃO!')
elif media >= 7.0 and media <= 10:
    print('Voçê está APROVADO!') 