#Operações aplicados no programa
from .biblioteca.funcao import *
from lista.variaveis import *


def adiciona():
    while True:
        limpar()
        cpf = int(input(f'CPF do proprietario: '))
        if verifica(cpf):
            print('CPF ja adicionado, consulte o CPF ja existente.')
            continue
        else:
            while True:
                nome_pessoas = input('Digite o nome do proprietário: ').strip()
                opcao = int(input('Deseja adicionar um veículo? [1-Sim/2-Não] '))
                if opcao == 1:
                    while True:
                        modelo_veiculo = input('Digite o modelo do veículo: ').strip()
                        placa = input('Digite a placa do veículo: ').strip()
                        descricao_car = input('Descreva o veículo: ')
                        if verifica(placa=placa):
                            print("Placa já cadastrada!!!")
                            continue

                        veiculo[placa] = (modelo_veiculo, descricao_car)

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
                    error_opcao()
        break


def editar():
    while True:
        limpar()
        menu('Editar',['[1] - CPF', '[2] - Nome', '[3] - Veículo', '[0] - voltar'])
        opcao = int(input("Digite a opção desejada: "))
        cpf = int(input("Digite o CPF casastrado: "))
        match opcao:
            case 1:
                cpf_novo = int(input("Digite o novo CPF: "))
                print("Verificando...")
                if verifica(cpf):
                    print('[OK] CPF')
                    if verifica(cpf_novo):
                        print('[OK] CPF')
                        print(edita_dado(cpf, cpf_novo=cpf_novo))
                    else:
                        error_dado()
                else:
                    error_dado()
            case 2:
                nome_pessoas = input("Novo nome: ").strip()
                if verifica(cpf):
                    print('[OK] CPF')
                    print(edita_dado(cpf, nome=nome_pessoas))
                else:
                    error_dado()
            case 3:
                placa_velha = int(input("Placa registrada: "))
                placa = int(input("Placa nova: "))
                modelo_veiculo = input("Modelo do veículo: ").strip()
                descricao_car = input("Descrição do veículo: ")

                if verifica(cpf):
                    print('[OK] CPF')
                    if verifica(placa=placa):
                        print('[OK] Placa')
                        veiculo[placa] = [modelo_veiculo, descricao_car]
                        if verifica(placa=placa_velha) == False:
                            print('[OK] Placa nova')
                            print(edita_dado(cpf, placa=placa_velha, veiculo=veiculo))
                        else:
                            error_dado_existente()
                    else:
                        error_dado()
                else:
                    error_dado()
            case 0:
                print('Voltando...')
                break
            case _:
                error_opcao()
        break


def excluir():
    while True:
        limpar()
        menu('Excluir', ['[1] - Tudo', '[2] - Veículo', '[0] - Voltar'])
        opcao = int(input('O que deseja excluir?: '))
        cpf = int(input('Digite o CPF cadastrado: '))
        if opcao == 1:
            if verifica(cpf=cpf):
                if cpf in dados.keys():
                    excluir_dados(cpf)
                    print('Dados excluidos')
                    break
                else:
                    print('CPF não encontrado')
        elif opcao == 2:
            if verifica(cpf=cpf):
                print('[OK] CPF')
                placa = int(input("Digite a placa do veículo que deseja excluir: "))
                if verifica(cpf, placa=placa):
                    excluir_dados(cpf, placa)
                    break
                else:
                    error_dado()
            else: 
                error_dado()
        elif opcao == 0:
            print('Voltando....')
            break
        else:
            error_opcao()


# Listar dados
def listar():
    limpar()
    cpf = int(input('Digite o CPF da pessoa a ser procurada: '))
    print(pesquisar_dados(cpf))