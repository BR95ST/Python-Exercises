indice = int(input("indice: "))
contNum = 1
contPrimo = 0
contIndex = 1
loop = True
while loop:
    for a in range(1, contNum + 1, 1):
        if contNum % a == 0:
            contPrimo += 1
    if contPrimo == 2:
        contIndex += 1
        if contIndex == indice:
            loop = False
    else:
        contPrimo = 0
    contNum += 1
print(contNum - 1, contIndex)