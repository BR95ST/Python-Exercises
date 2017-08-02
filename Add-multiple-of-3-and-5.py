lista = []
definitivo = []
i, j = 0, 0
while i < 1000:
    lista.append(i)
    i += 1  
while j < 1000:
    if lista[j] % 3 == 0 or lista[j] % 5 == 0:
        definitivo.append(lista[j])            
    j += 1
print(sum(definitivo))
