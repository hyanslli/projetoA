#Funções aplicadas no programa
from lista.dados import *
from lista.variaveis import *
from prettytable import PrettyTable
from .Erros import *


def menu(titulo=None, opcoes=None):
    menu_instance = PrettyTable()
    if titulo and opcoes:
        menu_instance.add_column(f'{titulo}', opcoes)
        menu_instance.align[f'{titulo}'] = 'l'
        print(menu_instance)
    else:
        menu_instance.add_column('Cadastro Detran', [
            '[1] - Adicionar',
            '[2] - excluir',
            '[3] - Pesquisar',
            '[4] - Alterar',
            '[5] - Listar',
            '[0] - Sair'])
        menu_instance.align['Cadastro Detran']= 'l'
        print(menu_instance)


def limpar():
    veiculo.clear()
    propietario.clear()
    lista.clear()


# Verifica se o dado ja esta no DB
def verifica(cpf=None, nome=None, placa=None):
    l = []
    if cpf:
        if cpf in dados:
            return True
        else:
            return False
    elif nome:
        if nome in dados.values():
            return True
        else:
            return False
    elif placa:
        if placa in dados.values()['veiculo']:
            return True
        else:
            return False
    else:
        if verifica(cpf):
            if type(placa) == list:
                for p in placa:
                    if verifica(placa=p):
                        l.append(f'A placa {p} já tem um proprietario')
                if len(l) == 0:
                    return True
                else:
                    return l
        else:
            return 'CPF já cadastrado!!!'


# Adicionando propietario
def adicionar_prop(nome, cpf, veiculo=None):
    if veiculo:
        propietario['nome'] = nome
        propietario['cpf'] = cpf
        propietario['veiculo'] = veiculo

        dados[cpf] = propietario
    else:
        propietario['nome'] = nome
        propietario['cpf'] = cpf

        dados[cpf] = propietario
    return 'Adicionado com sucesso!!!'


# Exclusão de dados
def excluir_dados(cpf, placa=None):
    if cpf:
        del dados[cpf]
    else:
        del dados[cpf]['veiculos'][placa]
    return 'Excluido com sucesso'


# Pesquisar
def pesquisar_dados(cpf=None, nome=None, placa=None):
    if cpf:
        try:
            return dados[cpf]
        except:
            error_dado()
    elif nome:
        for dado in dados:
            if nome in dados[dado]:
                lista.append(dados[dado])
            else:
                error_dado()
        return lista
    else:
        for dado in dados:
            if placa in dados[dado]['veiculo']:
                return dados[dado]
