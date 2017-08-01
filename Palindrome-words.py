palavra = input("Digite uma palavra: ")
if palavra[0::1] == palavra[::-1]:
    print("A palavra",palavra," eh palindrome")
else:
    print("A palavra não e palindrome")
