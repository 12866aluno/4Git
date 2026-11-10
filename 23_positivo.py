# Atividade 23 — Número positivo
#
# Crie uma função chamada eh_positivo(numero).
#
# A função deverá retornar:
# - True, se o número for maior que zero;
# - False, caso contrário.
#
# Dica:
# Comece usando if e else.

def eh_positivo(numero):
  if numero > 0:
    return True
  elif numero < 0:
    return False
  else:
    return "Você digitou 0, é um valor nulo"

print(eh_positivo(-5))