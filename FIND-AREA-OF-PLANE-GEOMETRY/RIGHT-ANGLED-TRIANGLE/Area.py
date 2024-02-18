# Area of Right angled triangle
#A = Area, a = Vertical line, b = base line of triangle

while True:
    a = float(input("Vertical Side of triangle a: "))
    b = float(input("Base side of triangle b: "))
    print("Area of Right angled triangle is A: ", ((a * b) /  2))
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break