# Importando biblioteca para manipulação de arquivos
import os

# Função para exibir o menu
def exibir_menu():
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

# Função para adicionar tarefa
def adicionar_tarefa(tarefa, lista_tarefas):
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para exibir tarefas
def exibir_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função para remover tarefa
def remover_tarefa(lista_tarefas):
    exibir_tarefas(lista_tarefas)
    if not lista_tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= indice <= len(lista_tarefas):
            tarefa_removida = lista_tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

# Função principal
def main():
    lista_tarefas = []

    while True:
        exibir_menu()

        opcao = input("Digite a opção desejada (1-4): ")

        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefa, lista_tarefas)
        elif opcao == "2":
            exibir_tarefas(lista_tarefas)
        elif opcao == "3":
            remover_tarefa(lista_tarefas)
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
