import math
a, b, c = 0, 0, 0
tempList = []
for a in range(0, 3, 1):
    tempList.append(float(input()))
tempList.sort()
tempList.reverse()
a = tempList[0]
b = tempList[1]
c = tempList[2]
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if pow(a,2) == pow(b,2) + pow(c,2):
        print("TRIANGULO RETANGULO")
    if pow(a,2) > pow(b,2) + pow(c,2):
        print("TRIANGULO OBTUSANGULO")
    if pow(a,2) < pow(b,2) + pow(c,2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
