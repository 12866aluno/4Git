# Atividade 14 — Sequência até um limite
#
# Crie uma função chamada mostrar_sequencia(limite).
#
# A função deverá mostrar todos os números de 1
# até o valor recebido.
#
# Exemplo:
# mostrar_sequencia(5)
#
# deverá mostrar:
# 1
# 2
# 3
# 4
# 5
#
# Dica:
# Use range(1, limite + 1).


def mostrar_sequencia(limite):
    for c in range(0, limite + 1):
        print(c)


mostrar_sequencia(int(input("Insira o Nº limite: ")))
