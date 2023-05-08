#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    a = float(input("Length of upper base: "))
    b = float(input("Length of Lower base: "))
    c = float(input("Length of side c(right): "))
    d = float(input("Length of side d(left): "))
    P = (a + b + c + d)
    print("Perimeter of trapezoid: ", P)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break