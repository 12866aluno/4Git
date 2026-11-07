# Atividade 10 — Total de uma compra
#
# Crie uma função chamada calcular_compra(preco, quantidade).
#
# A função deverá calcular e mostrar o valor total da compra.
#
# Dica:
# Multiplique preco por quantidade.

def calcular_compra(preco,quant):
  total = preco*quant
  return total

total_compra = calcular_compra(float(input("Preço: ")),float(input("Quantidade: ")))

print(f"Total da compra: {total_compra:.2f}")