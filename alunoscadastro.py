# Lista de alunos
alunos = []

# Função para adicionar aluno
def adicionar_aluno(nome, idade, notas):
    aluno = {'Nome': nome, 'Idade': idade, 'Notas': notas}
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para exibir informações de todos os alunos
def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Notas: {aluno['Notas']}")

# Função principal
def main():
    while True:
        print("\n1. Adicionar Aluno")
        print("2. Ver Lista de Alunos")
        print("3. Sair")

        opcao = input("Digite a opção desejada (1-3): ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            notas = input("Digite as notas do aluno (separadas por vírgula): ").split(',')
            notas = [float(nota) for nota in notas]
            
            adicionar_aluno(nome, idade, notas)
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            print("Saindo do sistema de cadastro de alunos. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
