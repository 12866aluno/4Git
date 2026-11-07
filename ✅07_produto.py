# Atividade 07 — Produto
#
# Crie uma função chamada mostrar_produto(nome, preco).
#
# A função deverá mostrar o nome e o preço de um produto.
#
# Exemplo de saída:
#
# Produto: Shampoo
# Preço: R$ 18.50
#
# Dica:
# Use dois parâmetros e respeite a ordem dos argumentos na chamada.


def mostrar_produto(nome, preco):
    print(f"{nome}: R${preco:.2f}")


mostrar_produto("café", 50)
mostrar_produto("arroz", 24)
mostrar_produto("feijão", 15)
