#Right-Rectangular-Prism
# Length = l, Height = h, Width = w, 
# Surface Area = A Volume = V, Space Diagonal = d. 
import math

while True:
    l = float(input("Enter the length of right rectangular prism"))
    h = float(input("Enter the height of right rectangular prism"))
    d = float(input("Enter the Space Diagonal of right rectangular prism"))
    w = (math.sqrt((d**2) - (h**2) - (l**2)))
    print("Width of right rectangular prism is, w: ", w)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break