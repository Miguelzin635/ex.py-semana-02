nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
nota3 = float(input("Digite sua 3° nota: "))
nota4 = float(input("Digite sua 4° nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 

if media < 6:
    print("Reprovado")
else:
    print("Aprovado")
