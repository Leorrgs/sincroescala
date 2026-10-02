import json
from pathlib import Path

path_bd = Path(__file__).parent / "BD" / "funcionario_bd.json"
funcionarios = []

def _carregar_funcionario():
    if not path_bd.exists():
        return []
    
    with open(path_bd,"r", encoding="utf-8") as arquivo:
       return json.load(arquivo)
   
def _pedir_id():
    return int(input("digite o id do funcionário que deseja excluir: "))
   

def cadastrar_funcionarios():
    funcionarios = _carregar_funcionario()
    print("======================================")
    print("     CADASTRO DE FUNCIONARIOS")
    print("======================================")
    print("")
    nome = input("digite o nome do funcionario: ")
    
    proximo_id = max((f["id"] for f in funcionarios), default=0) + 1
    funcionarios.append({"id": proximo_id, "nome":nome})
    
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)
    print(f"O nome cadastrado foi: {funcionarios}")
    print("======================================")
    print("você gostaria de adicionar um novo funcionário?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_funcionarios()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")
        
def listar_funcionarios():
    funcionarios = _carregar_funcionario()
    for f in funcionarios :
        print(f"id: {f['id']} - nome: {f['nome']}")
            
def excluir_funcionarios():
    funcionarios = _carregar_funcionario()
    id_excluir = _pedir_id()
    
    funcionario = next((f for f in funcionarios if f["id"] == id_excluir),None)
    funcionarios.remove(funcionario)
    
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)
    
            
