from sys import exit
import json

class IDCliente:
    def __init__(self):
        self.id = 0
    def updateID(self):
        self.id += 1
        return self.id

class IDTarefa:
    def __init__(self):
        self.id = 0
    def updateID(self):
        self.id += 1
        return self.id

id_cliente = IDCliente()
id_tarefa = IDTarefa()

class User:
    def __init__(self, idC, nome, email):
        self.idC = idC
        self.nome = nome
        self.email = email
    def __str__(self):
        return json.dumps({"ID": self.idC, "Nome": self.nome, "Email": self.email})

class Task:
    def __init__(self, idT, titulo, descricao, status, usuario):
        self.idT = idT
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.usuario = usuario
    def __str__(self):
        return json.dumps({"ID": self.idT, "Título": self.titulo, "Descrição": self.descricao, "Status": self.status, "Usuário": self.usuario})

def separarMenu():
    print("\n" * 10)

def menu():
    while True:
        print("-----------------------------")
        print("| 1 - Gerenciar usuários    |")
        print("| 2 - Gerenciar tarefas     |")
        print("| 3 - Sair                  |")
        print("-----------------------------")
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                separarMenu()
                menu_usuarios()
            elif opcao == 2:
                separarMenu()
                menu_tarefas()
            elif opcao == 3:
                print("Saindo do sistema, até a próxima!")
                exit()
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite um valor válido!")

def menu_usuarios():
    while True:
        print("-----------------------------------")
        print("| 1 - Cadastrar usuário           |")
        print("| 2 - Listar usuários cadastrados |")
        print("| 3 - Voltar                      |")
        print("-----------------------------------")
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                addUsers()
            elif opcao == 2:
                viewUsers()
            elif opcao == 3:
                return
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite um valor válido!")
            

def menu_tarefas():
    while True:
        print("--------------------------------------------")
        print("| 1 - Cadastrar tarefa                     |")
        print("| 2 - Listar todas as tarefas cadastradas  |")
        print("| 3 - Voltar                               |")
        print("--------------------------------------------")
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                addTask()
            elif opcao == 2:
                viewTask()
            elif opcao == 3:
                return
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite um valor válido!")

def addUsers():
    try:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
    except ValueError:
        print("Digite um valor válido!")
 
    
    novoIDC = id_cliente.updateID()

    try:    
        arq = open("users.json", "r")
        usuariosRetirados = json.load(arq)
        arq.close()
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        usuariosRetirados = []
    except json.JSONDecodeError:
        print("Erro no Arquivo.")
        usuariosRetirados = []

    usuariosRetirados.append({
        "ID": novoIDC, 
        "Nome": nome, 
        "Email": email
    })
    arq = open("users.json", "w")
    json.dump(usuariosRetirados, arq)
    arq.close()
  

def viewUsers():
    try:
        arq = open("users.json", "r")
        print("Esses são os usuários cadastrados: \n")
        usuariosRetirados = json.load(arq)
        print(usuariosRetirados)
        arq.close()
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
 

def findUser(idProcurado):
    try:
        arq = open("users.json", "r")
        usuariosRetirados = json.load(arq)
        for usuario in usuariosRetirados:
            if usuario["ID"] == idProcurado:
                # Achou!
                arq.close()
                return usuario
        arq.close()
    except FileNotFoundError:
        print("Arquivo de usuário não encontrado.")
        arq.close()
        return None

def addTask():
    try:
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        status = input("Digite o status da tarefa (Pendente - Em andamento - Concluído): \n")
    except ValueError:
        print("Digite um valor válido!")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
    
    viewUsers()
    id_cliente_procura = int(input("Digite o ID do usuário responsável pela tarefa: ")) 
    EncontreCliente = findUser(id_cliente_procura)
    if EncontreCliente == None:
        print("Usuário não encontrado. Tarefa não pode ser criada.")
  
    else:
        #cliente encontrado!
        novoIDT = id_tarefa.updateID()
        try:
            arq = open("tasks.json", "r")
            TarefasCadastradas = json.load(arq)
            arq.close()
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado.")
            TarefasCadastradas = []
        except json.JSONDecodeError:
            print("Erro no Arquivo.")
            TarefasCadastradas = []

        TarefasCadastradas.append({
            "ID": novoIDT, 
            "Título": titulo, 
            "Descrição": descricao,
            "Status": status,
            "Tarefa de Usuário": EncontreCliente
        })
        arq = open("users.json", "w")
        json.dump(TarefasCadastradas, arq)
        arq.close()

def viewTask():
    try:
        arq = open("tasks.json", "r")
        print("Essas são as tarefas cadastradas: \n")
        TarefasCadastradas = json.load(arq)
        print(TarefasCadastradas)
        arq.close()
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")

menu()