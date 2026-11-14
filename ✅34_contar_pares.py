# Atividade 34 — Contar números pares
#
# Crie uma função chamada contar_pares(limite).
#
# A função deverá retornar quantos números pares existem
# entre 1 e o limite informado.
#
# Dica:
# Use um contador dentro de um for.

def contar_pares(limite):
    cont_pares = 0
    for c in range(1, limite+1):
        if c % 2 == 0:
            cont_pares += 1
    return cont_pares


print(contar_pares(3))
