#Funções aplicadas no programa
from lista.dados import *
from lista.variaveis import *

def menu():
    menu_instance.add_column('Cadastro Detran', [
        '[1] - Adicionar', 
        '[2] - excluir', 
        '[3] - Pesquisar', 
        '[4] - Alterar', 
        '[5] - Listar', 
        '[0] - Sair'])
    menu_instance.align['Cadastro Detran']= 'l'
    print(menu_instance)


# Adicionando propietario
def adicionar_prop(nome, cpf, veiculo=None):
    if cpf in dados.keys():
        return '[ERROR] CPF já existente!!!'
    else:
        if veiculo:
            propietario[nome] = nome
            propietario[cpf] = cpf
            propietario['veiculo'] = veiculo

            dados[cpf] = propietario
        else:
            propietario[nome] = nome
            propietario[cpf] = cpf

            dados[cpf] = propietario

# Excluir Dados
def excluir_dados(nome, cpf, veiculo):
    del dados[cpf]
    del propietario[veiculo]
    