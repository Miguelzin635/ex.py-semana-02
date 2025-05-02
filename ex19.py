angulo = float(input("Digite o ângulo em graus: "))

if angulo > 0 and angulo < 90:
    print("O ângulo está no primeiro quadrante.")
elif angulo > 90 and angulo < 180:
    print("O ângulo está no segundo quadrante.")
elif angulo > 180 and angulo < 270:
    print("O ângulo está no terceiro quadrante.")
elif angulo > 270 and angulo < 360:
    print('O ângulo está no quarto quadrante.')
elif angulo == 0 or angulo == 360 or angulo == 180:
    print("O ângulo está sobre o eixo X.")
elif angulo == 90 or angulo == 270:
    print("O ângulo está sobre o eixo Y.")
elif angulo > 360 or angulo < 0:
    reduzido = angulo % 360
    voltas = angulo / 360 
    if reduzido > 0 and reduzido < 90:
        print("O ângulo está no primeiro quadrante.")
        print(f"O número de voltas é {abs(voltas):.1f}")       
    elif reduzido > 90 and reduzido < 180:
        print("O ângulo está no segundo quadrante.")
        print(f"O número de voltas é {abs(voltas):.1f}")             
    elif reduzido > 180 and reduzido <270:
        print("O ângulo está no terceiro quadrante.")
        print(f"O número de voltas é {abs(voltas):.1f}")       
    elif reduzido > 270 and reduzido < 360:
        print('O ângulo está no quarto quadrante.')
        print(f"O número de voltas é {abs(voltas):.1f}") 
    elif reduzido == 0 or reduzido == 360 or reduzido == 180:
        print("O ângulo está sobre o eixo X.")
        print(f"O número de voltas é {abs(voltas):.1f}")
    elif reduzido == 90 or reduzido == 270:
        print("O ângulo está sobre o eixo Y.")
        print(f"O número de voltas é {abs(voltas):.1f}")
if angulo >=0:
    print("Sentido anti-horário.")     
elif angulo < 0:
    print("Sentido horário.")

input("\nPressione Enter para fechar o programa...")
