#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    P = float(input("Perimeter of trapezoid: "))
    a = float(input("Length of upper base: "))
    b = float(input("Length of Lower base: "))
    c = float(input("Length of side c(right): "))
    d = (P - a - b - c)
    print("Length of side d(left): ", d)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break