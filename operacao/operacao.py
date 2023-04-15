#Operações aplicados no programa
from .biblioteca.funcao import *
from lista.variaveis import *

def cabecalho():
    menu()
    r = int(input("Digite a opção: "))
    return r

def adiciona():
    nome_pessoas = input('Digite o nome da Pessoa: ').strip()
    cpf = int(input(f'CPF do(a) {nome_pessoas}: '))
    while True:
        opcao = int(input('Deseja adicionar um veículo? [1-Sim/2-Não] '))
        if opcao == 1:
            modelo_veiculo = input('Digite o modelo do veículo: ').strip()
            placa = input('Digite a placa do veículo: ').strip()
            descricao_car = input('Descrva o veículo: ')

            veiculo['modelo']  = modelo_veiculo
            veiculo['placa']  = placa
            veiculo['descricao']  = descricao_car

            adicionar_prop(nome_pessoas, cpf, veiculo)
            break
        elif opcao == 2:
            adicionar_prop(nome_pessoas, cpf)
            break
        else:
            print('ERROR... Opção invalida. Digite apenas [1- para SIM | 2- para NÃO]: ')


