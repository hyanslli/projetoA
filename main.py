# Projeto Detra - De Willian Viana de Sousa e Josué Luiz Barbosa e Silva
from operacao.operacao import *

while True:
    menu()
    opcao = int(input("Digite a opção: "))
    match opcao:
        case 0:
            print('Saindo...')
            break
        case 1:
            adiciona()
        case 2:
            excluir()
        case 3:
            listar()
        case 4:
            editar()
        case _:
            error_opcao()
        