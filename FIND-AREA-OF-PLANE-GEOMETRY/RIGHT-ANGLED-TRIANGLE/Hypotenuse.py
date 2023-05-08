## Area of Right angled triangle
#A = Area, a = Vertical line, b = base line of triangle.
#c = Hypotenuse

import math

while True:
    a = float(input("Verticle Side of triangle a: "))
    b = float(input("Base side of triangle b: "))
    print("Length of Hypotenuse is ", math.sqrt((a**2) + (b**2)))

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break
