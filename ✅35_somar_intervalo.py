# Atividade 35 — Somar um intervalo
#
# Crie uma função que receba dois números:
# - início;
# - fim.
#
# A função deverá retornar a soma de todos os números
# existentes nesse intervalo, incluindo os extremos.
#
# Dica:
# Use range() e uma variável acumuladora.

def soma_intervalo(inicio, fim):
    soma = 0
    for c in range(inicio, fim+1):
        soma += c
    return soma


print(soma_intervalo(1, 5))
