#Cylinder
# Surface Area = A, r = radius, h = Height, Volume = V
# AL = Lateral Surface Area , AB = Bae Area, 
# π = 3.14 ( use 'Alt + 0960' for "π" sign.)
import math

while True:
    user_want_to_find = input("Select what to find? [Surface Area or A, radius or r, Height or h, Volume or V, Lateral Surface Area or AL, Base Area or AB]")
    π = 3.14

    if user_want_to_find == "Surface Area" or user_want_to_find == "A":
        r = float(input("Enter radius of cylinder r: "))
        h = float(input("Enter height of cylinder, h: "))
        A = ((2 * π * r * h) + (2 * π * (r**2)))
        print("Surface Area of Cylinder is, A: ", A)
    elif user_want_to_find == "radius" or user_want_to_find == "r":
        A = float(input("Enter Surface Area of cylinder, A: "))
        h = float(input("Enter height of cylinder, h: "))
        r = (((1/5) * (math.sqrt((h**2) + (2 * (A / π ))))) (h / 2))
        print("Radius of Cylinder is, r: ")
    elif user_want_to_find == "Height" or user_want_to_find =="h":
        V = float(input("Enter Volume of Cylender: "))
        r = float(input("Enter radius of cylinder r: "))
        h = (V / (π * (r**2)))
        print("Height of Cylinder is", h)
    elif user_want_to_find == "Volume" or user_want_to_find == "V":
        r = float(input("Enter radius of cylinder r: "))
        h = float(input("Enter height of cylinder, h: "))
        d = float(input("Enter Diameter of Cylinder: "))
        V = (π * ((d / 2)**2) * h)
        print("Volume of Cylinder is: ", V)
    elif user_want_to_find == "Latral Surafce Area" or user_want_to_find == "AL":
        r = float(input("Enter radius of cylinder r: "))
        h = float(input("Enter height of cylinder, h: "))
        AL = (2 * π * r * h)
        print("Lateral Surface area of Circle is: ",AL)
    elif user_want_to_find == "Base Area" or user_want_to_find == "AB":
        r = float(input("Enter radius of cylinder r: "))
        AB = (π * (r**2))
        print("Base Area of cylindr is: ", AB)
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break