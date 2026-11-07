# Atividade 11 — Verificar nota
#
# Crie uma função chamada verificar_nota(nota).
#
# A função deverá mostrar:
# - Aprovado, quando a nota for maior ou igual a 60;
# - Reprovado, nos demais casos.
#
# Dica:
# Use o parâmetro nota diretamente na condição do if.

def verificar_nota(nota):
  if nota >= 60:
    return "Aprovado"
  else:
    return "Reprovado"

situacao = verificar_nota(float(input("Nota: ")))

print(situacao)