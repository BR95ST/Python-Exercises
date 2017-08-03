num = int(input())
div = 2
conjunto = []
while num > 1:
    if num % div == 0:
        num = num/div
        if div not in conjunto:
            conjunto.append(div)
    else:
        div += 1        
conjunto.sort()
conjunto.reverse()
print(conjunto)
