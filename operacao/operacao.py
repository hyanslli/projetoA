#Operações aplicados no programa
from .biblioteca.funcao import *
from lista.variaveis import *

def cabecalho():
    menu()
    r = int(input("Digite a opção: "))
    return r

def adiciona():
    cpf = int(input(f'CPF do proprietario: '))
    if cpf in propietario.values():
        print('CPF ja adicionado, consulte o CPF ja existente.')
    else:
        while True:
            nome_pessoas = input('Digite o nome do proprietário: ').strip()
            opcao = int(input('Deseja adicionar um veículo? [1-Sim/2-Não] '))
            if opcao == 1:
                modelo_veiculo = input('Digite o modelo do veículo: ').strip()
                placa = input('Digite a placa do veículo: ').strip()
                descricao_car = input('Descrva o veículo: ')

                veiculo['modelo']  = modelo_veiculo
                veiculo['placa']  = placa
                veiculo['descricao']  = descricao_car

                adiciona = adicionar_prop(nome_pessoas, cpf, veiculo)

                if adiciona:
                    print(adiciona)
                else:
                    print('Informações adicionadas com sucesso!')
                break
            elif opcao == 2:
                adicionar_prop(nome_pessoas, cpf)
                print('Informações adicionadas com sucesso!')
                break
            else:
                print('ERROR... Opção invalida. Digite apenas [1- para SIM | 2- para NÃO]: ')

def excluir():
    while True:
        menu_excluir()
        opcao = int(input('O que deseja excluir?: '))
        if opcao == 1:
            cpf = int(input('Digite o CPF da pessoa que deseja excluir: '))
            if cpf in propietario.values():
                excluir_dados(cpf)
                print('Dados excluidos')
                break
            else:
                print('CPF não encontrado')
        elif opcao ==2:
            cpf = int(input('Digite o CPF da pessoa que deseja excluir: '))
            if cpf in dados.values():
                if veiculo in propietario.values():
                    excluir_dados(veiculo)
                    print('Dados excluidos')
                break
            else: 
                print('CPF não encontrado')
        elif opcao ==0:
            print('Operação cancelada')
            break
        else:
            print('ERROR... Opção invalida. Digite apenas [1- para TUDO | 2- para VEÍCULO]: ')

def listar():
    cpf = int(input('Digite o CPF da pessoa a ser procurada: '))
    pesquisar_dados(cpf)
    