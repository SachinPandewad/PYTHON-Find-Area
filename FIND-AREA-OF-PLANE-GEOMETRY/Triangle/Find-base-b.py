# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    A = float(input("Enter Area of Triangle A: "))
    hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
    b = (2 * (A / hb))
    print(" Length of base is, b = ", b)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    