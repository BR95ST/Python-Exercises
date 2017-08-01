import math
x1, x2 = float(input("x1: ")), float(input("x2: "))
y1, y2 = float(input("y1: ")), float(input("y2: "))
distance = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
print("Distance: %.4f"%distance)
