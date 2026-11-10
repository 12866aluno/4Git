# Atividade 20 — Maior entre dois números
#
# Crie uma função chamada maior(a, b).
#
# A função deverá retornar o maior dos 
# dois valores recebidos.
#
# Dica:
# Use if e else.

def maior(a, b):
  if a > b:
    return a
  elif b > a:
    return b
  else:
    return None

print(maior(9, 3))