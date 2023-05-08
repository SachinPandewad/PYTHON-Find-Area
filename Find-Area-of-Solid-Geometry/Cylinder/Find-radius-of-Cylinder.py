#Cylinder
# Surface Area = A, r = radius, h = Height, Volume = V
# AL = Lateral Surface, AB = Bae Area, 
# π = 3.14 ( use 'Alt + 0960' for "π" sign.)
import math

while True:
    π = 3.14
    A = float(input("Enter Surface Area of cylinder, A: "))
    h = float(input("Enter height of cylinder, h: "))
    r = (((1/5) * (math.sqrt((h**2) + (2 * (A / π ))))) (h / 2))
    print("Radius of Cylinder is, r: ")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break