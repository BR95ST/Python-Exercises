num = int(input())
div = 2
conjunto = [2]
while num > 1:
    if num % div == 0:
        num = num/div
    else:
        div += 1        
        conjunto.append(div)
conjunto.sort()
conjunto.reverse()
print(conjunto)
