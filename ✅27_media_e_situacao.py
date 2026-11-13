# Atividade 27 — Média e situação
#
# Crie duas funções:
#
# calcular_media(nota1, nota2)
# - deve retornar a média das duas notas.
#
# verificar_situacao(nota1, nota2)
# - deve usar a função calcular_media();
# - deve informar a situação do aluno.
#
# Dica:
# Uma função pode chamar outra função normalmente.

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# imaginei a média para aprovação sendo 7 ou mais, e a de recuperação sendo entre 5 e 7


def verificar_situacao(nota1, nota2):
    media_notas = calcular_media(nota1, nota2)
    if media_notas >= 7:
        return "Aprovado"
    elif media_notas < 7 and media_notas >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


print(verificar_situacao(5, 6))
