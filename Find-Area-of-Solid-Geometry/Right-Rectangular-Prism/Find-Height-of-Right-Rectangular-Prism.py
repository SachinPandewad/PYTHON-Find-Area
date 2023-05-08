#Right-Rectangular-Prism
# Length = l, Height = h, Width = w, 
# Surface Area = A Volume = V, Space Diagonal = d. 
import math

while True:
    w = float(input("Enter the width of right rectangular prism"))
    l = float(input("Enter the length of right rectangular prism"))
    d = float(input("Enter the Space Diagonal of right rectangular prism"))
    h = (math.sqrt((d**2) - (l**2) - (w**2)))
    print("Height of right rectangular prism is, h: ", h)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break