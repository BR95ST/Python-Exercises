import math
num1 = int(input())
num2 = int(input())
temp1 = pow(num1,num2)
temp2 = ""
temp3 = ""
temp2 = str(temp1)
temp1 = 0
for a in range(0, len(temp2), 1):
    temp3 = temp2[a:a+1:]
    temp1 += int(temp3)
print("Soma de todos os digitos: %d"%temp1)
    
