# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    A = float(input("Enter Area of Triangle A: "))
    b =  float(input("Enter lenght of  base. b: "))
    hb =  (2 * (A / b))
    print("Height of triangle is, hb = ", hb)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break