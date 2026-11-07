# Atividade 17 — Retornar o dobro
#
# Crie uma função chamada calcular_dobro(numero).
#
# A função deverá retornar o dobro do número recebido.
#
# Depois:
# 1. peça um número ao usuário;
# 2. envie o número para a função;
# 3. guarde o retorno em uma variável;
# 4. mostre o resultado.
#
# Dica:
# Dentro da função, use return em vez de print().

def calcular_dobro(numero):
    return numero * 2


resultado = (calcular_dobro(
    float(input("Insira um Nº para calcular o dobro: "))))

print(resultado)
