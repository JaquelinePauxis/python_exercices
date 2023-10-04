# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função principal
def main():
    while True:
        print("\n1. Converter Celsius para Fahrenheit")
        print("2. Converter Fahrenheit para Celsius")
        print("3. Sair")

        opcao = input("Digite a opção desejada (1-3): ")

        if opcao == "1":
            celsius = float(input("Digite a temperatura em graus Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {resultado:.2f}°F.")
        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F é igual a {resultado:.2f}°C.")
        elif opcao == "3":
            print("Saindo do conversor de temperatura. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
