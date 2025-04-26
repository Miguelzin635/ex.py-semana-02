preco = float(input("Digite o preço do produto: R$"))

if preco <= 50:
    novo_preco = preco + (preco * 0.05)
elif preco > 50 and preco <= 100:
    novo_preco = preco + (preco * 0.10)
else:
    novo_preco = preco + (preco * 0.15)

if novo_preco <= 80:
    print(f"O novo preço é R${novo_preco:.2f} \nE a classificação é: Barata")
elif novo_preco > 80 and novo_preco <= 120:
    print(f"O novo preço é R${novo_preco:.2f} \nE a classificação é: Normal")
elif novo_preco > 120 and novo_preco <= 200:
    print(f"O novo preço é R${novo_preco:.2f} \nE a classificação é: Caro")
else:
    novo_preco > 200
    print(f"O novo preço é R${novo_preco:.2f} \nE a classificação é: Muito Caro")

input("\nPressione Enter para sair do programa...")
