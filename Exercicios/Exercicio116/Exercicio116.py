# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo
# seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2
# opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from Exercicios.Exercicio116.lib.Interface import *
from Exercicios.Exercicio116.lib.Arquivo import *
from time import sleep

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[0;31mErro! Tente uma opção válida.\033[m')
    sleep(1)

