# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    P = float(input("Enter Perimeter P: "))
    b = float(input("Enter lenght of  base. b: "))
    c = float(input("Enter length of side c: "))
    a = (P - b - c)
    print("Lenght of side a is: ", a)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break