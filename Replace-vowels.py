palavra = input("Digite uma palavra")
aux = ""
for i in range(0, len(palavra), 1):
    if palavra[i] in 'aeiou':
        aux = aux + "*"
    else:
        aux = aux + palavra[i]
    i+=1
palavra = aux
print(palavra)
