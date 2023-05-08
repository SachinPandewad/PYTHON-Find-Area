# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 

while True:
    hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
    b =  float(input("Enter lenght of  base. b: "))
    A = ((hb * b) / 2)
    print("Area of Triangle is, A: ", A)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    