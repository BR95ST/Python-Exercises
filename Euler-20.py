num = int(input())
resul = num
temp = ""
temp1 = ""
temp2 = 0
while num > 1:
    resul = resul * (num - 1)
    num -= 1
temp = str(resul)
print("Fatorial: %s"%temp)
for a in range(0, len(temp), 1):
    temp1 = temp[a:a+1]
    temp2 += int(temp1)
print("Soma de todos os digitos do fatorial: %d"%temp2)
    








         
