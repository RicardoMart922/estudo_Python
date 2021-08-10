def aumetar(preco, porcentagem, boo=False):
    if boo:
        if preco >= 0:
            preco += (preco * porcentagem/100)
            return moeda(preco)
        else:
            return 0
    else:
        if preco >= 0:
            preco += (preco * porcentagem/100)
            return preco
        else:
            return 0


def diminuir(preco, porcentagem, boo=False):
    if boo:
        if preco >= 0:
            preco -= (preco * porcentagem/100)
            return moeda(preco)
        else:
            return 0
    else:
        if preco >= 0:
            preco -= (preco * porcentagem/100)
            return preco
        else:
            return 0


def dobro(preco, boo=False):
    if boo:
        if preco >= 0:
            return moeda(preco * 2)
        else:
            return 0
    else:
        if preco >= 0:
            return preco * 2
        else:
            return 0


def metade(preco, boo=False):
    if boo:
        if preco >= 0:
            return moeda(preco / 2)
        else:
            return 0
    else:
        if preco >= 0:
            return preco / 2
        else:
            return 0


def moeda(preco):
    return f'R${preco}'


def resumo(preco, aumento, reducao):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisando: {moeda(preco):>10}')
    print(f'Dobro do preço: {dobro(preco, True):>13}')
    print(f'Metade do preço: {metade(preco, True):>11}')
    print(f'{aumento}% de aumento: {aumetar(preco, aumento, True):>12}')
    print(f'{reducao}% de redução: {diminuir(preco, reducao, True):>12}')
    print('-' * 30)
