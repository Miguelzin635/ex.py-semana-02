salario = float(input("Digite o salário: "))

if salario < 500:
    novo_salario = salario + (salario * 0.3)
    print(f"Seu novo salário é: R${novo_salario:.2f}")
else:
    print("Você não tem direito a aumento.")

input("Pressione Enter para fechar o programa...")
