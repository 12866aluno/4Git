# Atividade 12 — Menu com match/case
#
# Crie uma função chamada mostrar_opcao(opcao).
#
# A função deverá mostrar uma das opções abaixo
# de acordo com o número recebido:
#
# 1 - Cadastrar
# 2 - Consultar
# 3 - Excluir
# 4 - Sair
#
# Dica:
# Use match/case e inclua um case _ para valores inválidos.

def mostrar_opcao(opcao):
  match opcao:
    case 1:
      return "Cadastrar"
    case 2:
      return "Consultar"
    case 3:
      return "Excluir"
    case 4:
      return "Sair"
    case _:
      return "Sair"


print("1 - Cadastrar\n2 - Consultar\n3 - Excluir\n4 - Sair")

opcao_selected = mostrar_opcao(int(input("Digite a opção e dê enter: ")))

print(opcao_selected)