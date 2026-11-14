# Atividade 40 — Desafio final
#
# Crie um pequeno sistema de produtos.
#
# O programa deverá ter funções para:
# - mostrar o menu;
# - calcular o total de uma compra;
# - calcular desconto;
# - calcular o preço final;
# - mostrar o resultado.
#
# O usuário deverá poder repetir operações
# até escolher sair.
#
# Dica:
# Divida o problema em pequenas funções antes
# de escrever o programa principal.

valor_total_da_compra = 0
valor_produto = 0
desconto = 0


def mostrar_menu():
    print("""================MENU================
    \n1 - Adicionar produto ao valor da compra
    \n2 - Calcular total da compra
    \n3 - Calcular desconto na compra
    \n4 - Calcular preço final
    \n5 - Mostrar valor final da compra
    \n6 - Sair""")
    print(" ")


def adicionar_produto():
    opcao = 0
    valor_produto = 0
    while opcao != 2:
        print("1 - Adicionar Produto\n2 - Sair")
        opcao = int(input("Digite a opção correspondente: "))
        if opcao == 1:
            match opcao:
                case 1:
                    valor_produto = float(input("Insira o valor do produto: "))
                    quantidade_produto = float(
                        input("Insira a quantidade deste produto: "))
                    valor_total_do_produto = valor_produto * quantidade_produto
        elif opcao > 2 or opcao < 1:
            print("Opção inválida, digite novamente")
    valor_produto = valor_total_do_produto


def calcular_total():
    valor_total_da_compra += valor_produto
    print(valor_total_da_compra)


def calcular_desconto_na_compra():
    desconto = 0
    print(""">>>>>>>DESCONTOS<<<<<<<
            \nR$100,00 ou acima: 10%
            \nR$500,00 ou acima: 20%
            \nR$1000,00 ou acima: 30%""")
    if valor_total_da_compra >= 1000:
        desconto = valor_total_da_compra * 30 / 100

    elif valor_total_da_compra >= 500:
        desconto = valor_total_da_compra * 20 / 100

    elif valor_total_da_compra >= 100:
        desconto = valor_total_da_compra * 10 / 100
    else:
        desconto = 0
    print(f"Desconto: {desconto}")


def calcular_preco_final():
    valor_total_da_compra -= desconto


def mostrar_valor_final_da_compra():
    print(valor_total_da_compra)


# --------------------------------------------------------------------------------
# -------------------------------PROGRAMA PRINCIPAL-------------------------------
# --------------------------------------------------------------------------------


opcao_menu = 0
while opcao_menu != 6:
    mostrar_menu()
    opcao_menu = int(input("Digite a sua opção desejada: "))
    match opcao_menu:
        case 1:
            adicionar_produto()
        case 2:
            calcular_total()
        case 3:
            calcular_desconto_na_compra()
        case 4:
            calcular_preco_final()
        case 5:
            mostrar_valor_final_da_compra()
        case 6:
            opcao_menu = 6
        case _:
            print("Opção inválida")
