# Atividade 16 — Contagem regressiva
#
# Crie uma função chamada contagem_regressiva(inicio).
#
# A função deverá mostrar os valores do número recebido
# até zero.
#
# Dica:
# Diminua a variável em 1 a cada repetição.

def contagem_regressiva(inicio):
    while inicio > 0:
        print(inicio)
        inicio -= 1


contagem_regressiva(7)
