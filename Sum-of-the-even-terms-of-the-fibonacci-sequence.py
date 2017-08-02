'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''
a = 1
b = 1
soma = 0
while b <= 4000000:
    a, b = b, a+b
    if a % 2 == 0:
        soma = soma + a
print(soma)
        
