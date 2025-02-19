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

    usuariosRetirados.append({
        "ID": novoIDC, 
        "Nome": nome, 
        "Email": email
    })
    with open("users.json", "w") as arq:
        json.dump(usuariosRetirados, arq, indent=4)
  

def viewUsers():
    try:
        arq = open("users.json", "r")
        print("Esses são os usuários cadastrados: \n")
        usuariosRetirados = json.load(arq)
        print(json.dumps(usuariosRetirados, indent=4))
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
 

def findUser(idProcurado):
    try:
        with open("users.json", "r") as arq:
            usuariosRetirados = json.load(arq)
            for usuario in usuariosRetirados:
                if usuario["ID"] == idProcurado:
                    # Achou!
                    arq.close()
                    return usuario
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
            with open("tasks.json", "r") as arq:
                TarefasCadastradas = json.load(arq)
        except FileNotFoundError:
            print("Arquivo de usuarios nao encontrado.")
            TarefasCadastradas = []

        TarefasCadastradas.append({
            "ID": novoIDT, 
            "Titulo": titulo, 
            "Descricao": descricao,
            "Status": status,
            "Tarefa de Usuario": EncontreCliente
        })
        arq = open("tasks.json", "w")
        json.dump(TarefasCadastradas, arq,indent=4)
        arq.close()

def viewTask():
    try:
        arq = open("tasks.json", "r")
        print("Essas são as tarefas cadastradas: \n")
        TarefasCadastradas = json.load(arq)
        print(json.dumps(TarefasCadastradas, indent=4))
        arq.close()
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
