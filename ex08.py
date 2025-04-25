print("Salário\t\t\tPercentual de Aumento")
print("-----------------------------------------------")
print("Até R$ 300,00\t\t\t35%")
print("Acima de R$ 300,00\t\t15%")
print("-----------------------------------------------")

salario = float(input("Digite o salário: R$"))

if salario <= 300:
    print(f"\nSeu novo salário é: R${salario + (salario * 0.35):.2f}")
else:
    print(f"\nSeu novo salário é: R${salario + (salario * 0.15):.2f}")

input("\nPressione qualquer tecla para fechar o programa...")
