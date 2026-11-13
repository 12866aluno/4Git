# Atividade 29 — Preço final
#
# Crie duas funções:
#
# calcular_desconto(valor, percentual)
# calcular_preco_final(valor, percentual)
#
# A segunda função deverá usar a primeira e retornar
# o preço final após o desconto.
#
# Dica:
# Subtraia o desconto do valor original.

def calcular_desconto(valor, percentual):
    desconto = valor * percentual / 100
    return desconto


def calcular_preco_final(valor, percentual):
    preco_final = valor - calcular_desconto(valor, percentual)
    return preco_final


print(calcular_preco_final(20, 2))
