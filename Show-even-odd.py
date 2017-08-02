inicio = 1
fim = int(input("Digite um numero"))
while inicio <= fim:
    if inicio % 2 == 0:
        print("Par: ",inicio)
    inicio = inicio + 1
inicio = 0
while inicio <= fim:
    if inicio % 2 != 0:
        print("Impar: ",inicio)
    inicio = inicio + 1