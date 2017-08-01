import random
chute = 0
ver = random.randint(1, 100)
while chute != ver:
    chute = int(input("Digite o numero:"))
    if chute == ver:
        print("Você venceu!")
    else:
        if chute > ver:
            print("Alto")
        else:
            print("Baixo")
