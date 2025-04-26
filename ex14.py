print("Tipo\t\t\tDescrição\t\t\tRendimento mensal")
print("--------------------------------------------------------------------------------")
print("1\t\t\tPoupança\t\t\t\t3%")
print("2\t\tFundos de renda fixa\t\t\t\t4%")
print("3\t\tFundos de renda variável\t\t\t5%")
print("--------------------------------------------------------------------------------")

escolha = int(input("\nEscolha o tipo de investimento: "))

if escolha == 1:
    valor = float(input("\nDigite o valor de investimento desejado: R$"))
    valor_final = valor + (valor * 0.03)
    print(f"O valor corrigido de acordo com a poupança é R${valor_final:.2f}")
elif escolha == 2:
    valor = float(input("\nDigite o valor de investimento desejado: R$"))
    valor_final = valor + (valor * 0.04)
    print(f"O valor corrigido de acordo com os fundos de renda fixa é R${valor_final:.2f}")
elif escolha == 3:
    valor = float(input("\nDigite o valor de investimento desejado: R$"))
    valor_final = valor + (valor * 0.05)
    print(f"O valor corrigido de acordo com os fundos de renda variável é R${valor_final:.2f}")
else: print("\nOpção inválida!")

input("\nPressione Enter para fechar o programa...")
