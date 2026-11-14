# Atividade 30 — Validar nota
#
# Crie uma função chamada nota_valida(nota).
#
# A função deverá retornar True apenas para valores
# entre 0 e 100.
#
# Depois use essa função em um while para obrigar
# o usuário a informar uma nota válida.
#
# Dica:
# A função pode retornar diretamente o resultado
# de uma comparação.

def nota_valida(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False


var_nota = False
# criei uma variável para aqui abaixo no código ela armazenar o valor de return da função

while var_nota == False:
    var_nota = nota_valida(float(input("Insira sua nota: ")))
    if var_nota == False:
        print("Nota inválida, tente novamente: ")
    else:
        print(var_nota)
