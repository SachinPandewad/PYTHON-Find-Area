#Right-Rectangular-Prism
# Length = l, Height = h, Width = w, 
# Surface Area = A Volume = V, Space Diagonal = d. 
import math

while True:
    w = float(input("Enter the width of right rectangular prism"))
    h = float(input("Enter the height of right rectangular prism"))
    l = float(input("Enter the length of right rectangular prism"))
    A = (2 * ((w * l) + (h * l) + (hw) ))
    print("Surface Area of right rectangular prismis: ", A)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break