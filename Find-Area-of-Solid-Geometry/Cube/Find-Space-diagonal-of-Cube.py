# Cube
# A = Surface Area of Cube, a = Edge of cube
# d = space diagonal, V = volume

import math
while True:
    a = float(input("Enter Length of edge of cube, a: "))
    d = (math.sqrt(3) * a)
    print("Space Diagonal of Cube is, d: ", d)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    