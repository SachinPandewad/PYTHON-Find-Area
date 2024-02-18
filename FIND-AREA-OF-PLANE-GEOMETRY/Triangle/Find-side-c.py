# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    P = float(input("Enter Perimeter P: "))
    a = float(input("Enter length of side a: "))
    b = float(input("Enter lenght of  base. b: "))
    c = (P - a - b)
    print("length of side c is: ", c)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break