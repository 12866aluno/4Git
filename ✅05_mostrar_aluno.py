# Atividade 05 — Mostrar aluno
#
# Crie uma função chamada mostrar_aluno(nome).
#
# A função deverá receber o nome de um aluno e mostrar:
#
# Aluno: nome_recebido
#
# Faça três chamadas da função usando nomes diferentes.
#
# Dica:
# Não use input() dentro da função nesta atividade.
# Envie o nome no momento da chamada.


def mostrar_aluno(nome):
    Aluno = nome
    print(f"Aluno: {Aluno}")


mostrar_aluno(input("Nome do aluno: "))
