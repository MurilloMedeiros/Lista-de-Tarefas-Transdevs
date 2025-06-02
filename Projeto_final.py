def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("--> Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    print('\n')
    print("-" * 50)
    print(f"{ ' ' *20}Lista de Tarefas{' ' * 15}")
    print("-" * 50)
    for indice, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{indice} - {tarefa}")
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, indice):
    lista_de_tarefas.pop(indice - 1)
    return lista_de_tarefas

def exibir_menu():
    print("-" * 50)
    print("Escolha uma opção:\n"
          "1 - Inserir nova tarefa\n"
          "2 - Listar Tarefas\n"
          "3 - Deletar tarefa\n"
          "4 - Sair")
    print("-" * 50)

def confirmar_delecao(tarefa):
    confirmacao = input(f"Tem certeza que deseja deletar a tarefa '{tarefa}'? (S/N): ")
    return confirmacao.upper() == "S"

lista_de_tarefas = []
continuar = True
print("-" * 50)

print("Bem-vinde à sua lista de tarefas!")
print('\n')

while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: \n")
    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        if len(lista_de_tarefas) == 0:
            print("Não há tarefas para deletar.")
        else:
            listar_tarefas(lista_de_tarefas)
            tarefa = input('Insira o número da tarefa que deseja deletar: ')
            if not tarefa.isnumeric():
                print("Número inválido! Tente novamente.")
            elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:
                print("Número inválido! Tente novamente")
            else:
                indice = int(tarefa)
                if confirmar_delecao(lista_de_tarefas[indice - 1]):
                    lista_de_tarefas = deletar_tarefa(lista_de_tarefas, indice)
                    print("Tarefa deletada com sucesso!")
                else:
                    print("Operação cancelada.")
    elif opcao == "4":
        continuar = False
    else:
        print("\n")
        print("Opção inválida! Tente novamente, por favor")
    print('\n')
