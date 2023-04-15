#Projeto Detra - De Willian Viana de Sousa e Josué Luiz Barbosa e Silva
from operacao.operacao import *
from lista.variaveis import opcao

while True:
    opcao = cabecalho()
    match opcao:
        case 0:
            print('Saindo...')
            break
        case 1:
            adiciona()
        case 2:
            excluir()
        