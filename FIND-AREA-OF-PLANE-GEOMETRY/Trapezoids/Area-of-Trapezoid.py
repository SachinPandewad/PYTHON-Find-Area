#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    a = float(input("Length of upper base: "))
    b = float(input("Length of Lower base: "))
    h = float(input("Length of Hieght: "))
    Area = (((a + b)/ 2) * h )
    print("Area of Trapezoid is: ", Area)
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break