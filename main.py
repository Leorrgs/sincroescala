
def apresenta_menu():
    print("======================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("======================================")
    print("")
    print("1. Cadastrar funcionário📝")
    print("2. Listar funcionário📝📝")
    print("0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu

def cadastrar_funcionarios():
    funcionarios = input("digite o nome do funcionario: ")
    print("O nome cadastrado foi: {funcionários}")
    
def listar_funcionarios():
    print("listando funcionarios")

def sair():
    print("saindo do sistema de gestão de escala⏏️")
#=======================================================================

opcao_menu = apresenta_menu()

match opcao_menu:
    case "1":
        cadastrar_funcionarios()
    case "2":
        listar_funcionarios()
    case "0":
        print("Quase final de semana!")
    case _:
        print("Opção Inválida.")
        
