nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

print("A média é: ", media)

if media >= 0.0 and media < 4.0:
    print("Reprovado")
elif media >= 4.0 and media < 7.0:
    print("Exame")
elif media >= 7.0 and media < 10.0:
    print("Aprovado")

input("\nPressione qualquer tecla para sair...")
