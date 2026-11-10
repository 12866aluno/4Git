# Atividade 26 — Área do triângulo
#
# Crie uma função chamada calcular_area_triangulo(base, altura).
#
# A função deverá retornar a área de um triângulo.
#
# Dica:
# Use a fórmula:
# (base * altura) / 2

def calcular_area_triangulo(base, altura):
  area = (base * altura)/2
  return area

print(f"{calcular_area_triangulo(3, 7):.2f}")