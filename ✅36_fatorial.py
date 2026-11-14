# Atividade 36 — Fatorial
#
# Crie uma função chamada fatorial(numero).
#
# A função deverá retornar o fatorial de um número
# inteiro não negativo.
#
# Exemplo:
# 5! = 5 * 4 * 3 * 2 * 1
#
# Dica:
# Comece o acumulador com 1.

def fatorial(numero):
    numero = numero
    acumulador = 1
    while numero < 1:
        numero = int(input(
            "Insira um Nº para que seja calculado seu fatorial, deve ser maior que 0: "))
    for c in range(1, numero):
        acumulador += acumulador * c
    return acumulador


print(fatorial(0))
