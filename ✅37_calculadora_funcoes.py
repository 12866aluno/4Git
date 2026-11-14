# Atividade 37 — Calculadora com funções
#
# Crie funções separadas para:
# - somar;
# - subtrair;
# - multiplicar;
# - dividir.
#
# Depois use match/case para escolher a operação.
#
# Dica:
# Cada função deve ter apenas uma responsabilidade.

def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


numeros = [(float(input("Insira o primeiro número: "))),
           (float(input("Insira o segundo número: ")))]

print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
operacao = int(input("Agora, escolha a operação desejada: "))

match operacao:
    case 1:
        print(somar(numeros[0], numeros[1]))
    case 2:
        print(subtrair(numeros[0], numeros[1]))
    case 3:
        print(multiplicar(numeros[0], numeros[1]))
    case 4:
        print(dividir(numeros[0], numeros[1]))
