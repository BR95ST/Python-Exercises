import math

#Incomplete

a, b, c = float(input("A: ")), float(input("B: ")), float(input("C: "))
delta = math.pow(b, 2) - 4 * a * c
print("Delta: ",delta)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("x1 = %.2f, x2 = %.2f"%(x1, x2))
if delta < 0:
    print("Não tem raizes reais")
if delta == 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("x1 = %.2f, x2 = %.2f"%(x1, x2))
