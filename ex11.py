print("Salário\t\t\t\t\t\tPercentual de aumento")
print("-----------------------------------------------------------------------------")
print("até R$ 300,00 \t\t\t\t\t\t15")
print("R$ 300,00 até R$ 600,00\t\t\t\t\t10")
print("R$ 600,00 até R$ 900,00\t\t\t\t\t5")
print("acima de R$ 900,00\t\t\t\t\t0")
print("-----------------------------------------------------------------------------")

salario = float(input("Digite o seu salário: R$"))

if salario <= 300:
    print(f"\nO aumento salarial é de R${salario * 0.15:.2f}")
    print(f"O novo salário é de R${salario + (salario * 0.15):.2f}")
elif salario > 300 and salario <= 600:
    print(f"\nO aumento salarial é de R${salario * 0.10:.2f}")
    print(f"O novo salário é de R${salario + (salario * 0.10):.2f}")
elif salario > 600 and salario <= 900:
    print(f"\nO aumento salarial é de R${salario * 0.05:.2f}")
    print(f"O novo salário é de R${salario + (salario * 0.05):.2f}")
else: 
    print("\nNão recebe aumento salarial")
    print(f"O novo salário é de R${salario}")

input("Pressione Enter para fechar o programa")
