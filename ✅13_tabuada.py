# Atividade 13 — Tabuada
#
# Crie uma função chamada mostrar_tabuada(numero).
#
# A função deverá mostrar a tabuada de 1 até 10
# do número recebido.
#
# Dica:
# Use for e range(1, 11).


def mostrar_tabuada(numero):
    for c in range(1, 11):
        print(f"{numero} × {c} = {numero*c}")


mostrar_tabuada(2)
