# Atividade 15 — Contagem crescente
#
# Crie uma função que receba um número.
#
# A função deverá fazer uma contagem de zero
# até o número recebido usando while.
#
# Dica:
# Comece com um contador igual a zero.


def contagem_crescente(num):
    c = 0
    while c < num:
        print(c)
        c += 1
    print(num)


contagem_crescente(int(input("Insira o número limite: ")))
