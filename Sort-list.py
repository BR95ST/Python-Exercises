myList = []
choise = 's'
while 's' in choise:
    print("Digite um número na lista")
    myList.append(int(input()))
    print("Deseja inserir mais numeros?")
    choise = input()
for i in range(0, len(myList), 1):
    for j in range(i + 1, len(myList), 1):
        if myList[i] > myList[j]:
            myList[i], myList[j] = myList[j], myList[i]
print(myList)
