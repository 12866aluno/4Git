# Atividade 39 — Sistema de notas
#
# Crie as funções:
#
# ler_nota()
# calcular_media()
# classificar_media()
# mostrar_resultado()
#
# Organize o programa principal para utilizar essas funções.
#
# Dica:
# Antes de programar, determine:
# - o que cada função recebe;
# - o que cada função retorna;
# - o que cada função apenas mostra.

# ----------------------------------------------------

# EU DEFINI QUE:
# MÉDIA > 10 = APROVADO
# MÉDIA < 10 E MÉDIA > 5 = RECUPERAÇÃO
# MÉDIA < 5 = REPROVADO


def ler_nota():
    soma = 0
    for c in range(1, 4):
        nota = float(input(f"Insira a {c}ª nota: "))
        soma += nota
        return soma


def calcular_media():
    media = 0
    media = soma / 3
    return media


def classificar_media():
    if media > 10:
        print("Aprovado")
    elif media < 10 and media > 5:
        print("Recuperação")
    else:
        print("Reprovado")


def mostrar_resultado():
    print(f"Seu resultado: {classificar_media()}")


ler_nota()

calcular_media()
classificar_media()
mostrar_resultado()
