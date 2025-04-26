salario = float(input("Digite seu salário: R$"))

if salario <= 300:
    novo_salario = salario + (salario * 0.50)
    print(f"Seu salário com o aumento é: {novo_salario:.2f}")
elif salario > 300 and salario <= 500:
    novo_salario = salario + (salario * 0.40)
    print(f"Seu salário com o aumento é: {novo_salario:.2f}")
elif salario > 500 and salario <= 700:
    novo_salario = salario + (salario * 0.30)
    print(f"Seu salário com o aumento é: {novo_salario:.2f}")
elif salario > 700 and salario <= 800:
    novo_salario = salario + (salario * 0.20)
    print(f"Seu salário com o aumento é: {novo_salario:.2f}")
elif salario > 800 and salario <= 1000:
    novo_salario = salario + (salario * 0.10)
    print(f"Seu salário com o aumento é: {novo_salario:.2f}")
else: 
    print(f"Seu salário com aumento é: {salario + (salario * 0.05):.2f}")

input("Pressione Enter para fechar o programa...")
