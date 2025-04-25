print("1\tMédia entre os números digitados")

print("2\tDiferença do maior pelo menor")

print("3\tProduto entre os números digitados")

print("4\tDivisão do primeiro pelo segundo")

escolha = int(input("\nDigite o número referente ao problema: "))

if escolha == 1:
    print("\nMédia entre os números digitados:")
    n1 = float(input("Digite o 1º valor: "))
    n2 = float(input("Digite o 2º valor: "))
    media = (n1 + n2)/2
    print("A média entre", n1, "e", n2, "é: ",media)
elif escolha == 2:
    print("\nDiferença do maior pelo menor:")
    n1 = float(input("Digite o 1º valor: "))
    n2 = float(input("Digite o 2º valor: "))
    if n1 > n2:
        print("A diferença entre", n1, "e", n2, "é: ", (n1 - n2))
    else: print("A diferença entre", n2, "e", n1, "é: ", (n2 - n1))
elif escolha == 3:
    print("\nProduto entre os números digitados:")
    n1 = float(input("Digite o 1º valor: "))
    n2 = float(input("Digite o 2º valor: "))
    produto = n1 * n2
    print("O produto entre", n1, "e", n2, "é:", produto)
elif escolha == 4:
    print("Divisão do primeiro pelo segundo")
    n1 = float(input("Digite o 1º valor: "))
    n2 = float(input("Digite o 2º valor: "))
    divisao = n1 / n2
    print("A divisão entre", n1, "e", n2, "é: ", divisao)

input("Digite Enter para sair do programa...")
