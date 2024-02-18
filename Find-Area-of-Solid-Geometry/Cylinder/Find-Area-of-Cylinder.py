#Cylinder
# Surface Area = A, r = radius, h = Height, Volume = V
# AL = Lateral Surface, AB = Bae Area, 
# π = 3.14 ( use 'Alt + 0960' for "π" sign.)

while True:
    π = 3.14
    r = float(input("Enter radius of cylinder r: "))
    h = float(input("Enter height of cylinder, h: "))
    A = ((2 * π * r * h) + (2 * π * (r**2)))
    print("Surface Area of Cylinder is, A: ", A)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break