dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
contador = dividendo
resul = 0
while contador >= divisor:
     contador = contador - divisor
     resul += 1
print("Resultado: ", resul)
print("Resto: ", contador)
