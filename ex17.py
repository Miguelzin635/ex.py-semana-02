print("Bem-vindo ao sistema de aprovação de crédito!")

idade = int(input("\nDigite sua idade: "))
salario = float(input("Digite seu salário: R$"))
dividas = float(input("Digite o total de suas dívidas: R$"))
pagamentos = int(input("Digite o número de pagamentos realizados nos últimos 6 meses: "))

if idade >=25 and idade <= 60 and salario >= 3000:
    if dividas <= salario * 0.20 and pagamentos >= 2:
            print("Você foi aprovado!")
    elif dividas == 0 and pagamentos >= 0 and pagamentos <= 1:
        print("Você foi aprovado!")
    else: print("Você foi reprovado!")
else:
    print("Você foi reprovado!")

input("\nPressione Enter para fechar o programa...")   
