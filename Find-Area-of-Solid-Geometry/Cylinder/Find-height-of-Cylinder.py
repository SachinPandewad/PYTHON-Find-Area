#Cylinder
# Surface Area = A, r = radius, h = Height, Volume = V
# AL = Lateral Surface, AB = Bae Area, 
# π = 3.14 ( use 'Alt + 0960' for "π" sign.)

while True:
    π = 3.14
    V = float(input("Enter Volume of Cylender: "))
    r = float(input("Enter radius of cylinder r: "))
    h = (V / (π * (r**2)))
    print("Height of Cylinder is", h)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break
