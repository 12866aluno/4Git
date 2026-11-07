# Atividade 09 — Média de três notas
#
# Crie uma função chamada calcular_media(nota1, nota2, nota3).
#
# A função deverá calcular e mostrar a média de três notas.
#
# Dica:
# Some as três notas e divida o resultado por 3.

def calcular_media(nota1,nota2,nota3):
  media = (nota1+nota2+nota3)/3
  return media

print(f"{calcular_media(3.23,5,7):.2f}")