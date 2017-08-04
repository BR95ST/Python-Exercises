a = 1
b = 1
aStr = ""
cont = 1
while len(aStr) < 1000:
    a, b = b, a + b
    cont += 1
    aStr = str(a)
print("indice: %d numero: %d"%(cont, a))
