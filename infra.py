from sys import exit
import json

class User:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Task:
    def __init__(self, id, titulo, descricao, status, user):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.user = user

def separarMenu():
    print("\n" * 5)
    print("-" * 50)

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

class IDCliente:
    def __init__(self):
        self.id = 1
    def updateID(self):
        self.id += 1
        return self.id

id_cliente = IDCliente()

class IDTarefa:
    def __init__(self):
        self.id = 1
    def updateID(self):
        self.id += 1
        return self.id

id_tarefa = IDTarefa()

def addUsers():
    arq = open("usuarios.txt", "a")
    try:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
    except ValueError:
        print("Digite um valor válido!")
        menu()
    
    NovoUser_id = id_cliente.updateID()
    arq.write(f"ID: {NovoUser_id} - NOME: {nome} - EMAIL: {email}\n")
    arq.close()

def viewUsers():
    try:
        arq = open("usuarios.txt", "r")
        print("Esses são os usuários cadastrados: \n")
        print(arq.read())
        arq.close()
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

def findUser(id):
    try:
        arq = open("usuarios.txt", "r")
        for linha in arq:
            if f"ID: {id}" in linha:
                # achou o usuario
                arq.close()
                return linha.strip()
        arq.close()
    except FileNotFoundError:
        print("Arquivo de usuário não encontrado.")
        return None

def addTask():
    arq = open("tarefas.txt", "a")
    try:
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        status = input("Digite o status da tarefa (Pendente - Em andamento - Concluído): \n")
    except ValueError:
        print("Digite um valor válido!")
        menu()
    
    viewUsers()
    IDCliente_Procura = int(input("Digite o ID do usuário responsável pela tarefa: ")) 
    finder = findUser(IDCliente_Procura)
    if finder == None:
        print("Usuário não encontrado. Tarefa não pode ser criada.")
        menu()
    else:
        novoTask_id = id_tarefa.updateID()
        ClienteEncontrado = finder.split(" - ")[1].split(": ")[1]
        arq.write(f"Cliente: {ClienteEncontrado} - ID da Tarefa: {novoTask_id} - TÍTULO: {titulo} - DESCRIÇÃO: {descricao} - STATUS: {status}\n")
    arq.close()

def viewTask():
    try:
        arq = open("tarefas.txt", "r")
        print("Essas são as tarefas cadastradas: \n")
        print(arq.read())
        arq.close()
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")