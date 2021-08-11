from Exercicios.Exercicio116.lib.Interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido(a)', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao tentar escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
