#A = Area, a = Vertical line, b = base line of triangle.
#c = Hypotenuse, Perimeter = c
import math

while True:
    a = float(input("vertical Side of triangle a: "))
    b = float(input("Base side of triangle b: "))
    print("Perimeter if Right Angled Triangle, P is ", (a + b) + (math.sqrt((a**2) + (b**2))) )
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    