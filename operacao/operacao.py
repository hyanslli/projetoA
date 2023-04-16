#Operações aplicados no programa
from .biblioteca.funcao import *
from lista.variaveis import *


def cabecalho():
    menu()
    r = int(input("Digite a opção: "))
    return r


def adiciona():
    limpar()
    cpf = int(input(f'CPF do proprietario: '))
    if verifica(cpf):
        print('CPF ja adicionado, consulte o CPF ja existente.')
    else:
        while True:
            nome_pessoas = input('Digite o nome do proprietário: ').strip()
            opcao = int(input('Deseja adicionar um veículo? [1-Sim/2-Não] '))
            if opcao == 1:
                while True:
                    modelo_veiculo = input('Digite o modelo do veículo: ').strip()
                    placa = input('Digite a placa do veículo: ').strip()
                    descricao_car = input('Descrva o veículo: ')

                    veiculo[placa] = [modelo_veiculo, descricao_car]
                    opcao = int(input("Deseja continuar adicionando veículos? [0 - Não] "))
                    if opcao == 0:
                        break
                adiciona = adicionar_prop(nome_pessoas, cpf, veiculo)
                print(adiciona)
                break
            elif opcao == 2:
                adicionar_prop(nome_pessoas, cpf)
                print('Informações adicionadas com sucesso!')
                break
            else:
                print('ERROR... Opção invalida. Digite apenas [1- para SIM | 2- para NÃO]: ')


def excluir():
    limpar()
    while True:
        menu('Excluir', ['[1] - Tudo', '[2] - Veículo', '[0] - Voltar'])
        opcao = int(input('O que deseja excluir?: '))
        if opcao == 1:
            cpf = int(input('Digite o CPF da pessoa que deseja excluir: '))
            if verifica(cpf=cpf):
                excluir_dados(cpf)
                print('Dados excluidos')
                break
            else:
                print('CPF não encontrado')
        elif opcao ==2:
            cpf = int(input('Digite o CPF do dono do veículo que deseja excluir: '))
            if verifica(cpf=cpf):
                placa = int(input("Digite a placa dio veículo que deseja excluir: "))
                excluir_dados(cpf, placa)
                print('Dados excluidos')
                break
            else: 
                print('CPF não encontrado')
        elif opcao == 0:
            print('Voltando....')
            break
        else:
            print('ERROR... Opção invalida. Digite apenas [1- para TUDO | 2- para VEÍCULO]: ')

def listar():
    limpar()
    cpf = int(input('Digite o CPF da pessoa a ser procurada: '))
    pesquisar_dados(cpf)
    