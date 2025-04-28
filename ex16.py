print("Programa de concessão de bolsa de estudos!")

media = float(input("\nDigite sua média final: "))
renda = float(input("Digite sua renda familiar mensal: "))
horas_servico = int(input("Digite as horas de serviço comunitário prestadas: "))

if media >= 8.5 and renda <= 2500:
    print("Elegível para bolsa de estudos!")
elif media >= 8.0 and media <= 8.4 and horas_servico >= 30 and renda <= 2500:
    print("Elegível para bolsa de estudos!")
else:
    print("Não elegível para bolsa de estudos!")

input("\nPressione Enter para fechar o programa...")
