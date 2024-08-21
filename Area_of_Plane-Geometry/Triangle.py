# A = Area, b = base length, hb = Height perp. to base
# a = lenght of side a, c = length of side c.
# P = Perimeter 


def triangle_Area ():
    hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
    b =  float(input("Enter lenght of  base. b: "))
    A = ((hb * b) / 2)
    print("Area of Triangle is, A: ", A)

def triangle_Perimeter():
        a = float(input("Enter length of side a: "))
        b = float(input("Enter lenght of  base. b: "))
        c = float(input("Enter length of side c: "))
        P = (a + b + c)
        print("Perimeter of Triangle is: ", P)

def triangle_BaseLen():
        A = float(input("Enter Area of Triangle A: "))
        hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
        b = (2 * (A / hb))
        print(" Length of base is, b = ", b)

def triangle_height():
        A = float(input("Enter Area of Triangle A: "))
        b =  float(input("Enter lenght of  base. b: "))
        hb =  (2 * (A / b))
        print("Height of triangle is, hb = ", hb)
def triangle_SideALen():
        P = float(input("Enter Perimeter P: "))
        b = float(input("Enter lenght of  base. b: "))
        c = float(input("Enter length of side c: "))
        a = (P - b - c)
        print("Lenght of side a is: ", a)

def triangle_SideCLen():
        P = float(input("Enter Perimeter P: "))
        a = float(input("Enter length of side a: "))
        b = float(input("Enter lenght of  base. b: "))
        c = (P - a - b)
        print("length of side c is: ", c)


while True:
    user_want_to_find = input("Select what to find? [Area or A, Perimeter or P, base length or b, height or hb, length of side a or a, length of side c or c ]")

    if user_want_to_find == "Area" or user_want_to_find == "A":
        triangle_Area()
    elif user_want_to_find == "Perimeter" or user_want_to_find == "P":
        triangle_Perimeter()
    elif user_want_to_find == "base length" or  user_want_to_find == "b":
        triangle_BaseLen()
    elif user_want_to_find == "Height" or user_want_to_find == "hb":
        triangle_height()
    elif user_want_to_find == "length of side a " or user_want_to_find == "a":
        triangle_SideALen()
    elif user_want_to_find == "length of side c" or user_want_to_find == "c":
        triangle_SideCLen()
    else:
        print("Enter correct input.")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break