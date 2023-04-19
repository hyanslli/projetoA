#Operações aplicados no programa
from .biblioteca.funcao import *
from lista.variaveis import *


def operacao_complementar_listagem(dado):
    fields_names = ['Nome', 'CPF', 'Veículos-placas']
    if type(dado) == dict:
        for item in dado:
            list_keys = []
            if item == 'veiculos':
                for key in dado[item].keys():
                    list_keys.append(key)
                lista_dados_temp.append(list_keys)
            else:
                lista_dados_temp.append(dado[item])
        lista_geral.append(lista_dados_temp)
        menu(fields_names=fields_names, opcoes=lista_geral)
    else:
        for item in dado:
            list_keys = []
            for k in item:
                if k == 'veiculos':
                    for key in item[k].keys():
                        list_keys.append(key)
                    lista_dados_temp.append(list_keys)
                else:
                    lista_dados_temp.append(item[k])
            lista_geral.append(lista_dados_temp)
        menu(fields_names=fields_names, opcoes=lista_geral)
    limpar()


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
                    print(error_opcao())
            break


def editar():
    while True:
        limpar()
        menu(titulo='Editar',opcoes=['[1] - CPF', '[2] - Nome', '[3] - Veículo', '[0] - voltar'])
        opcao = int(input("Digite a opção desejada: "))
        cpf = int(input("Digite o CPF casastrado: "))
        match opcao:
            case 1:
                cpf_novo = int(input("Digite o novo CPF: "))
                print("Verificando...")
                if verifica(cpf):
                    print('[OK] CPF')
                    if verifica(cpf_novo) == False:
                        print('[OK] CPF NOVO')
                        print(edita_dado(cpf, cpf_novo=cpf_novo))
                    else:
                        print(error_dado())
                else:
                    print(error_dado())
            case 2:
                nome_pessoas = input("Novo nome: ").strip()
                if verifica(cpf):
                    print('[OK] CPF')
                    print(edita_dado(cpf, nome=nome_pessoas))
                else:
                    print(error_dado())
            case 3:
                placa_velha = input("Placa registrada: ")
                placa = input("Placa nova: ")
                modelo_veiculo = input("Modelo do veículo: ").strip()
                descricao_car = input("Descrição do veículo: ")

                if verifica(cpf):
                    print('[OK] CPF')
                    if verifica(placa=placa):
                        print('[OK] Placa')
                        veiculo[placa] = [modelo_veiculo, descricao_car]
                        if verifica(placa=placa_velha):
                            print('[OK] Placa nova')
                            print(edita_dado(cpf, placa=placa_velha, veiculo=veiculo))
                        else:
                            print(error_dado_existente())
                    else:
                        print(error_dado())
                else:
                    print(error_dado())
            case 0:
                print('Voltando...')
                break
            case _:
                print(error_opcao())


def excluir():
    while True:
        limpar()
        menu(titulo='Excluir', opcoes=['[1] - Tudo', '[2] - Veículo', '[0] - Voltar'])
        opcao = int(input('O que deseja excluir?: '))
        cpf = int(input('Digite o CPF cadastrado: '))
        if opcao == 1:
            if verifica(cpf=cpf):
                if cpf in dados.keys():
                    print(excluir_dados(cpf))
                    break
                else:
                    print('CPF não encontrado')
        elif opcao == 2:
            if verifica(cpf=cpf):
                print('[OK] CPF')
                placa = input("Digite a placa do veículo que deseja excluir: ")
                if verifica(cpf, placa=placa):
                    print(excluir_dados(cpf, placa))
                    break
                else:
                    print(error_dado())
            else: 
                print(error_dado())
        elif opcao == 0:
            print('Voltando....')
            break
        else:
            print(error_opcao())


# Listar dados
def listar():
    while True:
        limpar()
        menu(titulo='Listar', opcoes=['[1] - Por CPF', '[2] - Por nome', '[3] - Por placa', '[0] - voltar'])
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                cpf = int(input('Digite o CPF da pessoa a ser procurada: '))
                if verifica(cpf):
                    dado = pesquisar_dados(cpf)
                    operacao_complementar_listagem(dado)
                else:
                    error_dado()
            case 2:
                nome_pessoas = input("Nome do Proprietario: ").strip()
                dado = pesquisar_dados(nome=nome_pessoas)
                operacao_complementar_listagem(dado)
            case 3:
                placa = input("Placa do veículo: ").strip()
                if verifica(placa=placa):
                    dado = pesquisar_dados(placa=placa)
                    operacao_complementar_listagem(dado)
                else:
                    error_dado()
            case 0:
                print("Voltando...")
                break
            case _:
                print(error_opcao())