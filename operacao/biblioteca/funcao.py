#Funções aplicadas no programa
from lista.dados import *
from lista.variaveis import *
from prettytable import PrettyTable
from .Erros import *


def menu(titulo=None, fields_names=None, opcoes=None):
    menu_instance = PrettyTable()
    if titulo and opcoes:
        menu_instance.add_column(f'{titulo}', opcoes)
        menu_instance.align[f'{titulo}'] = 'l'
        print(menu_instance)
    elif fields_names:
        menu_instance.field_names = fields_names
        for i in opcoes:
            menu_instance.add_row([i[0], i[1], i[2]])
        print(menu_instance)
    else:
        menu_instance.add_column('Cadastro Detran', [
            '[1] - Adicionar',
            '[2] - excluir',
            '[3] - Pesquisar/listar',
            '[4] - Alterar',
            '[0] - Sair'])
        menu_instance.align['Cadastro Detran']= 'l'
        print(menu_instance)


def limpar():
    veiculo.clear()
    propietario.clear()
    lista.clear()
    lista_geral.clear()
    lista_dados_temp.clear()



"""
Mexendo com o DB
"""


# Verifica se o dado ja esta no DB
def verifica(cpf=None, nome=None, placa=None):
    if len(dados) != 0:
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
        elif cpf and placa:
            if placa in dados[cpf]['veiculos']:
                return True
            else:
                return False
        else:
            for item in dados:
                if len(dados[item]) != 0:
                    if placa in dados[item]['veiculos']:
                        return True
                    else:
                        return False
    else:
        return False


# Adicionando propietario
def adicionar_prop(nome, cpf, veiculo=None):
    if veiculo:
        propietario['nome'] = nome
        propietario['cpf'] = cpf
        propietario['veiculos'] = veiculo.copy()

        dados[cpf] = propietario.copy()
    else:
        propietario['nome'] = nome
        propietario['cpf'] = cpf
        propietario['veiculos'] = {}

        dados[cpf] = propietario.copy()
    return 'Adicionado com sucesso!!!'


# Edição de dados
def edita_dado(cpf, nome=None, cpf_novo=None, placa=None, veiculo=None):
    if cpf_novo:
        temp_dado = dados[cpf].copy()
        del dados[cpf]
        temp_dado['cpf'] = cpf_novo
        dados[cpf_novo] = temp_dado.copy()
        return 'Feito com sucesso'
    elif nome:
        dados[cpf]['nome'] = nome
        return 'Feito com sucesso'
    else:
        del dados[cpf]['veiculos'][placa]
        dados[cpf]['veiculos'][veiculo.keys()[0]] = veiculo.values().copy()
        return 'Feito com sucesso'


# Exclusão de dados
def excluir_dados(cpf, placa=None):
    if cpf and placa == None:
        del dados[cpf]
    else:
        dados[cpf]['veiculos'].pop(placa)
    return 'Excluido com sucesso'


# Pesquisar Dados
def pesquisar_dados(cpf=None, nome=None, placa=None):
    if cpf:
        try:
            return dados[cpf]
        except:
            error_dado()
    elif nome:
        for dado in dados:
            if nome == dados[dado]['nome']:
                lista.append(dados[dado])
        return lista
    else:
        for dado in dados:
            if placa in dados[dado]['veiculos']:
                return dados[dado]
