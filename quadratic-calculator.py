import math



x = float()
a = float(input("What's A? "))
b = int(input("What's B? "))
c = int(input("What's C? "))

x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2
L = [x1, x2]

print(L)
