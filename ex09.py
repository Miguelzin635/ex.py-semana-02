saldo_medio = float(input("Digite seu saldo médio: "))

if saldo_medio > 400:
    acima400 = saldo_medio * 30/100
    
    print("Seu saldo médio é: ", saldo_medio)
    
    print("Seu valor de crédito é: ", acima400)
elif saldo_medio <= 400 and saldo_medio > 300:
    entre400_300 = saldo_medio * 25/100
    
    print("Seu saldo médio é: ", saldo_medio)
    
    print("Seu valor de crédito é: ", entre400_300)
elif saldo_medio <= 300 and saldo_medio > 200:
    entre300_200 = saldo_medio * 20/100

    print("Seu saldo médio é: ", saldo_medio)
    
    print("Seu valor de crédito é: ", entre300_200)
elif saldo_medio <= 200:
    ate200 = saldo_medio * 10/100

    print("Seu saldo médio é: ", saldo_medio)
    
    print("Seu valor de crédito é: ", ate200)

input("\nAperta qualquer tecla para fechar o programa...")
