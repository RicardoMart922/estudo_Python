# Crie um programa que tenha uma função fatorial() que receba
# dois parâmetros: o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.
def fatorial(num=1, show=False):
    """
    => Calcula o Fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: o valor do Fatorial de um número num.
    """
    print('-' * 30)
    print(f'{num}! = ', end='')
    if show:
        fat = 1
        while num != -1:
            if num == 0:
                break
            if num != 1:
                print(f'{num} x ', end='')
            else:
                print(f'{num} = ', end='')
            fat *= num
            num -= 1
        return fat
    else:
        fat = 1
        while num != -1:
            if num == 0:
                break
            fat *= num
            num -= 1
        return fat


print(fatorial(5, False))
