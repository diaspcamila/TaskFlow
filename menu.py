import infra
from sys import exit

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
                infra.addUsers()
            elif opcao == 2:
                infra.viewUsers()
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
                infra.addTask()
            elif opcao == 2:
                infra.viewTask()
            elif opcao == 3:
                return
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite um valor válido!")


menuPrincipal()