# Atividade 21 — Menor entre três números
#
# Crie uma função que receba três números.
#
# A função deverá retornar o menor deles.
#
# Dica:
# Compare os valores usando estruturas condicionais.

def menor_tres(n1, n2, n3):
  if n1 < n2 and n1 < n3:
    return n1
  elif n2 < n1 and n2 < n3:
    return n2
  elif n3 < n1 and n3 < n2:
    return n3
  else:
    return "Os três números são iguais"

print(menor_tres(5, 5, 5))