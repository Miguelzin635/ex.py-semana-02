custo_fabrica = float(input("Digite o custo de fábrica do carro: R$"))

print("\nSiga a tabela abaixo para verificar o percentual de aumento dependendo do valor inserido: ")
print("\nCusto de Fábrica\t\t\t% do distribuidor\t\t\t% dos impostos")
print("------------------------------------------------------------------------------------------------")
print("até R$ 12.000,00\t\t\t\t5\t\t\t\tIsento")
print("entre R$ 12.000,00 e R$ 25.000,00\t\t10\t\t\t\t15")
print("acima de R$ 25.000,00\t\t\t\t15\t\t\t\t20")
print("------------------------------------------------------------------------------------------------")

if custo_fabrica <= 12000:
    print(f"\nO custo do carro ao consumidor é: R${custo_fabrica + (custo_fabrica * 0.05):.2f}")
elif custo_fabrica > 12000 and custo_fabrica <= 25000:
    print(f"\nO custo do carro ao consumidor é: R${custo_fabrica + (custo_fabrica * 0.10) + (custo_fabrica * 0.15):.2f}")
else:
    print(f"\nO custo do carro ao consumidor é: R${custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.20):.2f}")

input("\nPressione Enter para fechar o programa...")
