print("Avaliador de risco de investimento.")

idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: R$"))
hist_dividas =  float(input("Digite o histórico de dívidas nos últimos 2 anos: R$"))

pontuacao = (salario / 1000) - (hist_dividas / 2000) + (idade / 2)

if idade >= 30 and idade <= 50 and salario > 10000 and hist_dividas == 0:
    print("\nBaixo risco.")
    print (f"Sua pontuação de crédito é: {pontuacao:.2f}")
elif idade >= 25 and idade <= 60 and salario >= 5000 and salario <= 10000 and hist_dividas < 5000:
    print("\nMédio risco.")
    print (f"Sua pontuação de crédito é: {pontuacao:.2f}")
    if pontuacao > 80:
        print("IMPORTANTE!!\n--> Você foi movido de categoria, como sua pontuação é maior que 80, sua nova classificação é Baixo risco.")
else:
    print ("\nAlto risco.")
    print (f"Sua pontuação de crédito é: {pontuacao:.2f}")
    if pontuacao > 80:
        print("IMPORTANTE!!\n--> Você foi movido de categoria, como sua pontuação é maior que 80, sua nova classificação é Médio risco.")
        
input("\nPressione Enter para fechar o programa...")
