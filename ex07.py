print("1\tMédia entre os dois números")
print("2\tDiferença do maior pelo menor")
print("3\tO produto entre os dois números")

escolha = int(input("\nEscolha a operação desejada: "))

if escolha == 1:
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A média entre {n1} e {n2} é: {(n1 + n2) / 2:.2f}")
    input("\nPressione qualquer tecla para fechar o programa...")
elif escolha == 2:
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    if n1 > n2:
        print(f"A diferença entre {n1} e {n2} é: {n1 - n2}")
    else: print(f"A diferença entre {n2} e {n1} é: {n2- n1}")
    input("\nPressione qualquer tecla para fechar o programa...")
elif escolha == 3:
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O produto entre {n1} e {n2} é: {n1 * n2:.2f}")
    input("\nPressione Enter para fechar o programa...")
else: 
    print("Opção inválida!")
