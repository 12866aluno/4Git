# Atividade 38 — Calculadora com menu repetitivo
#
# Use a calculadora da atividade anterior.
#
# Agora o menu deverá permanecer disponível até que
# o usuário escolha a opção de sair.
#
# Dica:
# Use while no programa principal.

def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


operacao = 0

while operacao != 5:

    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    operacao = int(input("Escolha a operação desejada: "))

    if operacao != 5 and operacao >= 1 and operacao <= 4:
        numeros = [(float(input("Insira o primeiro número: "))),
                   (float(input("Insira o segundo número: ")))]

        match operacao:
            case 1:
                print(f"Resultado: {somar(numeros[0], numeros[1]):.2f}")
            case 2:
                print(f"Resultado: {subtrair(numeros[0], numeros[1]):.2f}")
            case 3:
                print(f"Resultado: {multiplicar(numeros[0], numeros[1]):.2f}")
            case 4:
                print(f"Resultado: {dividir(numeros[0], numeros[1]):.2f}")

        print(" ")

    elif operacao > 5 or operacao < 1:
        print("Opção inválida")
    else:
        print("Até a próxima! ")
