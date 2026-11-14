# Atividade 31 — Validar idade
#
# Crie uma função chamada idade_valida(idade).
#
# Considere válidas apenas idades entre 0 e 120.
#
# Use essa função em um while para validar
# a idade digitada pelo usuário.
#
# Dica:
# Retorne True ou False.

def idade_valida(idade):
    if idade >= 0 and idade <= 120:
        return True
    else:
        return False


var_idade = False
# repeti o método que usei no exercício 30

while var_idade == False:
    var_idade = idade_valida(int(input("Qual a sua idade? ")))
    if var_idade == False:
        print("Ou tu ainda nem nasceu, ou tu é a pessoa mais velha do planeta, tá doidão? Digite uma idade válida: ")
    else:
        print(var_idade)
