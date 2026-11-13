# Atividade 22 — Número par
#
# Crie uma função chamada eh_par(numero).
#
# A função deverá retornar:
# - True, se o número for par;
# - False, caso contrário.
#
# Dica:
# Use o operador % para verificar o resto da divisão por 2.

def eh_par(numero):
  if numero % 2 == 0:
    return True
  elif numero % 2 != 0:
    return False

print(eh_par(44))