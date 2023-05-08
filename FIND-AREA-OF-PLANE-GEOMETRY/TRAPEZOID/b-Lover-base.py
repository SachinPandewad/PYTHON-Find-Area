#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    A = float(input("Area of Trapezoid is: "))
    a = float(input("Length of upper base: "))
    h = float(input("Length of Hieght: "))
    b = ((2 * (A / h)) - a)
    print("Length of Lower base: ", b)
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break