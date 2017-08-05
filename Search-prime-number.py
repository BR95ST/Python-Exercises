cont = 0
a = int(input())
for b in range(1, a + 1, 1):
    if a % b == 0:
        cont += 1
if cont == 2:
    print("Primo")
else:
    print("Não Primo")