#Cylinder
# Surface Area = A, r = radius, h = Height, Volume = V
# AL = Lateral Surface, AB = Bae Area, 
# π = 3.14 ( use 'Alt + 0960' for "π" sign.)

while True:
    π = 3.14
    r = float(input("Enter radius of cylinder r: "))
    AB = (π * (r**2))
    print("Base Area of cylindr is: ", AB)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break