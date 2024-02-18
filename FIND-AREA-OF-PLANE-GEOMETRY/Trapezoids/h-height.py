#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    A = float(input("Area of Trapezoid is: "))
    a = float(input("Length of upper base: "))
    b = float(input("Length of Lower base: "))
    h = (2 * (A / ( a + b)))
    print("Length of Hieght: ", h)
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break