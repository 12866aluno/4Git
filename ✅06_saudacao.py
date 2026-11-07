# Atividade 06 — Saudação
#
# Solicite o nome de uma pessoa usando input().
#
# Depois envie esse nome para uma função chamada saudar(nome).
#
# A função deverá mostrar uma mensagem de boas-vindas.
#
# Dica:
# O input() deve ficar fora da função.

name = input("Nome: ")


def saudar(name):
    print(f"Bem Vindo, {name}")


saudar(name)
