#Funções aplicadas no programa
from prettytable import PrettyTable
from lista.dados import *
from lista.variaveis import *

def menu():
    menu = PrettyTable()
    menu.add_column('Cadastro Detran', [
        '[1] - Adicionar', 
        '[2] - excluir', 
        '[3] - Pesquisar', 
        '[4] - Alterar', 
        '[5] - Listar', 
        '[0] - Sair'])
    menu.align['Cadastro Detran']= 'l'
    print(menu)


# Adicionando propietario
def adicionar_prop(nome, cpf, veiculo=None):
    if veiculo:
        propietario[nome] = nome
        propietario[cpf] = cpf
        propietario['veiculo'] = veiculo

        dados[cpf] = propietario
    else:
        propietario[nome] = nome
        propietario[cpf] = cpf

        dados[cpf] = propietario

