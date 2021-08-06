# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
# aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.
lista = list()
expressao = str(input('Informe a expressão: '))
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
