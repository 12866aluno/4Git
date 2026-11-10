# Atividade 25 — Área do retângulo
#
# Crie uma função chamada calcular_area(base, altura).
#
# A função deverá retornar a área de um retângulo.
#
# Dica:
# Crie uma variável local chamada area e depois retorne-a.

def calcular_area(base, altura):
  area = base * altura
  return area

print(f"{calcular_area(2, 6):.2f}")