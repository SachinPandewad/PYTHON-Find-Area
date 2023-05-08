#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    A = float(input("Area of Trapezoid is: "))
    b = float(input("Length of Lower base: "))
    h = float(input("Length of Hieght: "))
    a = ((2 * (A / h)) -b )
    print("Length of upper base: ", a)
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break