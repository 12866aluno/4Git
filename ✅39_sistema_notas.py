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
# MÉDIA >= 10: APROVADO
# MÉDIA < 10 E MÉDIA > 5: RECUPERAÇÃO
# MÉDIA < 6: REPROVADO


def ler_nota(nota1, nota2, nota3):
    return nota1 + nota2 + nota3


def calcular_media(soma_notas):
    return soma_notas / 3


def classificar_media(media):
    if media > 10:
        print("Aprovado")
    elif media < 10 and media > 5:
        print("Recuperação")
    else:
        print("Reprovado")


def mostrar_resultado():
    print(f"Seu resultado: {classificar_media()}")


soma_notas = ler_nota(float(input("Insira a 1ª Nota: ")), float(
    input("Insira a 2ª Nota: ")), float(input("Insira a 3ª Nota: ")))

media = calcular_media(soma_notas)

classificar_media(media)
