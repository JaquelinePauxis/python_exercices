# Projeto: Calculadora de Despesas
import os

# Função para adicionar despesa
def adicionar_despesa(despesas, categoria, valor):
    if categoria in despesas:
        despesas[categoria] += valor
    else:
        despesas[categoria] = valor

# Função para exibir resumo de despesas
def exibir_resumo(despesas):
    if not despesas:
        print("Nenhuma despesa registrada.")
    else:
        print("Resumo de Despesas:")
        for categoria, valor in despesas.items():
            print(f"{categoria}: R$ {valor:.2f}")

# Função principal
def main():
    despesas = {}

    while True:
        print("\n1. Adicionar Despesa")
        print("2. Ver Resumo de Despesas")
        print("3. Sair")

        opcao = input("Digite a opção desejada (1-3): ")

        if opcao == "1":
            categoria = input("Digite a categoria da despesa: ")
            try:
                valor = float(input("Digite o valor da despesa: "))
                adicionar_despesa(despesas, categoria, valor)
                print("Despesa registrada com sucesso!")
            except ValueError:
                print("Digite um valor válido.")
        elif opcao == "2":
            exibir_resumo(despesas)
        elif opcao == "3":
            print("Saindo da calculadora de despesas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
