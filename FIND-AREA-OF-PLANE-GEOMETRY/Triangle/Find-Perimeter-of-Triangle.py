# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    a = float(input("Enter length of side a: "))
    b = float(input("Enter lenght of  base. b: "))
    c = float(input("Enter length of side c: "))
    P = (a + b + c)
    print("Perimeter of Triangle is: ", P)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break