from sys import exit
import json

def separarMenu():
    print("\n" * 10)

def menuPrincipal():
    while True:
        print("-----------------------------")
        print("| 1 - Gerenciar usuários    |")
        print("| 2 - Gerenciar tarefas     |")
        print("| 3 - Sair                  |")
        print("-----------------------------")
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                menu_usuarios()
            elif opcao == 2:
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

class IDCliente:
    def __init__(self, arquivo="ids_cliente.json"):
        self.arquivo = arquivo
        self.id = self.carregarID()
    
    def carregarID(self):
        try:
            with open(self.arquivo, "r") as arq:
                ultimoID = json.load(arq)
                if isinstance(ultimoID, dict) and "ID" in ultimoID:
                    return int(ultimoID.get("ID", 0))
                else:
                    return 0
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return 0
        
    def salvarID(self):
        with open(self.arquivo, "w") as arq:
            json.dump({"ID": self.id}, arq)
    
    def updateID(self):
        if self.id is None:
            self.id = 0
        self.id += 1
        self.salvarID()
        return self.id

class IDTarefa:
    def __init__(self, arquivo="ids_tarefa.json"):
        self.arquivo = arquivo
        self.id = self.carregarID()
    
    def carregarID(self):
        try:
            with open(self.arquivo, "r") as arq:
                ultimoID = json.load(arq)
                if isinstance(ultimoID, dict) and "ID" in ultimoID:
                    return int(ultimoID.get("ID", 0))
                else:
                    return 0
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return 0

    def salvarID(self):
        with open(self.arquivo, "w") as arq:
            json.dump({"ID": self.id}, arq)

    def updateID(self):
        if self.id is None:
            self.id = 0
        self.id += 1
        self.salvarID()
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
    def __init__(self, idT, titulo, descricao, status, usuario_id):
        self.idT = idT
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.usuario_id = usuario_id

    def __str__(self):
        return json.dumps({"ID": self.idT, "Título": self.titulo, "Descrição": self.descricao, "Status": self.status, "Usuário ID": self.usuario_id})

opcoesDeStatus = ["Pendente", "Em andamento", "Concluido"]
opcoesDeDominios = ["com", "org", "net", "gov", "edu", "br"]
opcoesDeDomEmails = ["gmail", "hotmail", "outlook", "yahoo", "uol"]

def confirmaEmail(email):
    if "@" not in email or " " in email:
        return False
    email2 = email.split("@")
    if len(email2) != 2:
        return False
    email3 = email2[1].split(".")
    if len(email3) != 2:
        return False
    if email3[0] not in opcoesDeDomEmails or email3[1] not in opcoesDeDominios:
        return False
    return True

def addUsers():
    nome = input("Digite o nome do usuário: ")
    nome2 = nome.split()
    nome2 = ''.join(nome2)
    if not nome2.isalpha():
        print("Nome inválido. Tente novamente.")
        return
    
    email = input("Digite o email do usuário: ")
    if not confirmaEmail(email):
        print("Email inválido. Tente novamente.")
        return
    
    novoIDC = id_cliente.updateID()

    try:    
        with open("users.json", "r") as arq:
            usuariosRetirados = json.load(arq)
    except FileNotFoundError:
        usuariosRetirados = []
    except json.JSONDecodeError:
        usuariosRetirados = []

    usuariosRetirados.append({
        "ID": novoIDC, 
        "Nome": nome, 
        "Email": email
    })
    with open("users.json", "w") as arq:
        json.dump(usuariosRetirados, arq, indent=4)
    print("Usuario cadastrado com sucesso!")

def viewUsers():
    try:
        with open("users.json", "r") as arq:
            print("Esses são os usuários cadastrados: \n")
            usuariosRetirados = json.load(arq)
            for usuario in usuariosRetirados:
                print(f"ID: {usuario['ID']} - Nome: {usuario['Nome']} - Email: {usuario['Email']}")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

def findUser(idProcurado):
    try:
        with open("users.json", "r") as arq:
            idProcurado = int(idProcurado)
            usuariosRetirados = json.load(arq)
            for usuario in usuariosRetirados:
                if usuario["ID"] == idProcurado:
                    return usuario
        return None
    except FileNotFoundError:
        print("Arquivo de usuário não encontrado.")
        return None

def addTask():
    titulo = input("Digite o título da tarefa: ")    
    descricao = input("Digite a descrição da tarefa: ")
    status = input("Digite o status da tarefa (Pendente - Em andamento - Concluido): \n")
    if status not in opcoesDeStatus:
        print("Status inválido. Tente novamente.")
        return
    
    viewUsers()
    id_cliente_procura = input("Digite o ID do usuário responsável pela tarefa: ")
    if not id_cliente_procura.isnumeric():
        print("ID inválido. Tarefa não pode ser criada.")
        return 
    id_cliente_procura = int(id_cliente_procura)
    EncontreCliente = findUser(id_cliente_procura)
    if EncontreCliente is None:
        print("Usuário não encontrado. Tarefa não pode ser criada.")
    else:
        novoIDT = id_tarefa.updateID()
        try:
            with open("tasks.json", "r") as arq:
                TarefasCadastradas = json.load(arq)
        except FileNotFoundError:
            TarefasCadastradas = []
        except json.JSONDecodeError:
            TarefasCadastradas = []

        TarefasCadastradas.append({
            "ID": novoIDT, 
            "Titulo": titulo, 
            "Descricao": descricao,
            "Status": status,
            "Usuario ID": id_cliente_procura
        })
        with open("tasks.json", "w") as arq:
            json.dump(TarefasCadastradas, arq, indent=4)
        print("Tarefa cadastrada com sucesso!")

def findTask(idProcurado):
    try:
        with open("tasks.json", "r") as arq:
            TarefasCadastradas = json.load(arq)
            for tarefas in TarefasCadastradas:
                if tarefas["ID"] == idProcurado:
                    return f'ID: {tarefas["ID"]} - Título: {tarefas["Titulo"]} - Descrição: {tarefas["Descricao"]} - Status: {tarefas["Status"]} - Usuário ID: {tarefas["Usuario ID"]}'
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
        return None

def viewTask():
    try:
        with open("tasks.json", "r") as arq:
            print("Essas são as tarefas cadastradas: \n")
            TarefasCadastradas = json.load(arq)
            for tarefas in TarefasCadastradas:
                print(f"ID: {tarefas['ID']} - Título: {tarefas['Titulo']} - Descrição: {tarefas['Descricao']} - Status: {tarefas['Status']} - Usuario ID: {tarefas['Usuario ID']}")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")

menuPrincipal()