numBin = []
numDec = 0 
print("Insira um valor em decimal")
numDec = int(input())
while numDec >= 1:
    numBin.append(numDec % 2)
    numDec = numDec / 2
numBin.reverse()
for i in range(0, len(numBin), 1):
    print(numBin[i], end="")
