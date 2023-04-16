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
    if veiculo:
        propietario['nome'] = nome
        propietario['Cpf'] = cpf
        propietario['veiculo'] = veiculo

        dados[cpf] = propietario
    else:
        propietario['Nome'] = nome
        propietario['CPF'] = cpf

        dados[cpf] = propietario

# Excluir Dados
def menu_excluir():
    menu_instance = PrettyTable()
    coluna = ['[1] - Tudo do usuario', '[2] - Apenas Veículo', '[0] - Cancelar']
    menu_instance.add_column('        Excluir', coluna)
    menu_instance.align = 'l'
    print(menu_instance)


def excluir_dados(cpf):
    del dados[cpf]

    
# Pesquisar
def pesquisar_dados(cpf):
    if cpf in dados.keys():
        print(dados[cpf])
    else:
        print('CPF não encontrado, digite um cpf valido ou adicione o CPF atual.')