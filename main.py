from pathlib import Path

path_bd = Path("sincroescala/BD") / "funcionario_bd.txt"
funcionarios = []
sair_do_sistema = False

def apresenta_menu():
    print("======================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("======================================")
    print("")
    print("1. Cadastrar funcionário📝")
    print("2. Listar funcionário📝📝")
    print("3. Excluir funcinário🗑️")
    print("0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu

def cadastrar_funcionários():
    funcionário = input("digite o nome do funcionario: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
            arquivo.write(f"{funcionário}\n")
    funcionarios.append(funcionário)
    print(f"O nome cadastrado foi: {funcionário}")
    print("======================================")
    print("você gostaria de adicionar um novo funcionário?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_funcionários()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")
     
def listar_funcionários():
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_limpo = linha.strip()
            print(nome_limpo)
            
def excluir_funcionários():
    listar_funcionários()
    funcionário = input("qual funcionário você deseja deletar: ")
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in nomes :
            if linha.strip() == funcionário:
                linha = ""
            arquivo.write(linha)  
    
def sair():
    print("saindo do sistema de gestão de escala⏏️")
#=======================================================================
while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
        case "1":
            cadastrar_funcionários()
        case "2":
            listar_funcionários()
        case "3":
            excluir_funcionários()    
        case "0":
            sair()
            break
        case _:
            print("Opção Inválida.")
        
