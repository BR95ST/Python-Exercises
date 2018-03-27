def pot(x):
    return x**2

pot_ = lambda x: x**2

fat_ = lambda x: x*fat_(x-1) if x>1 else 1




#print(pot(3))
#print(pot_(5))
print(fat_(5))
