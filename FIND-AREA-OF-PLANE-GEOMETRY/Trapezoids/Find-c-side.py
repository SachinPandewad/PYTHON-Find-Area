#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    P = float(input("Perimeter of trapezoid: "))
    a = float(input("Length of upper base: "))
    b = float(input("Length of Lower base: "))
    d = float(input("Length of side d(left): "))
    c = (P - a - b - d)
    print("Length of side c(right): ", c)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break