# Atividade 04 — Número positivo, negativo ou zero
#
# Crie uma função chamada verificar_numero().
#
# A função deverá:
# 1. pedir um número ao usuário;
# 2. informar se ele é positivo, negativo ou zero.
#
# Dica:
# Use if, elif e else dentro da função.


def verificar_numero():
    num = float(input("Insira um número: "))
    if num < 0:
        print("Negativo")
    elif num > 0:
        print("Positivo")
    else:
        print("Nulo, ou seja, zero")


verificar_numero()
