# Atividade 24 — Maioridade
#
# Crie uma função chamada eh_maior_de_idade(idade).
#
# A função deverá retornar True ou False.
#
# Depois use essa função diretamente dentro de um if
# no programa principal.
#
# Dica:
# A função não precisa mostrar a resposta.
# Ela deve apenas retornar o resultado da verificação.

def eh_maior_de_idade(idade):
  if idade >= 18:
    return True
  elif idade < 18:
    return False

print(eh_maior_de_idade(19))