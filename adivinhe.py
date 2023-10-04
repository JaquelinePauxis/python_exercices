import random

# Função para gerar um número aleatório
def gerar_numero():
    return random.randint(1, 100)

# Função principal do jogo
def jogar_adivinhacao():
    numero_secreto = gerar_numero()
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")

    while True:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

# Função principal
def main():
    while True:
        print("\n1. Jogar Jogo de Adivinhação")
        print("2. Sair")

        opcao = input("Digite a opção desejada (1-2): ")

        if opcao == "1":
            jogar_adivinhacao()
        elif opcao == "2":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
