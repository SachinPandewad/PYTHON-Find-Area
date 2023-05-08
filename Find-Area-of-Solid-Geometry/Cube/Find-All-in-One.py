# Cube
# A = Surface Area of Cube, a = Edge of cube
# d = space diagonal, V = Volume of cube

import math
while True:
    user_want_to_find = input("Select what to find? [Surface Area of Cube or A, Edge of cube or a, Volume of cube or V, Space Diagonal or d]")

    if user_want_to_find == "Surface Area of Cube" or user_want_to_find == "A":
        a = float(input("Enter Length of edge of cube, a: "))
        A = (6 * (a**2))
        print("Surface area of Cube is, A = ", A)
    elif user_want_to_find == "Edge of cube" or user_want_to_find == "a":
        A = float(input("Enter Surface Area of Cube, A: "))
        a = (math.sqrt(A / 6))
        print("Length of edge of cube is, a: ", a)
    elif user_want_to_find == "Volume of cube" or user_want_to_find == "V":
        a = float(input("Enter Length of edge of cube, a: "))
        V = (a**3)
        print("Volume of Cube is, V: ", V)
    elif user_want_to_find == "Space Diagonal" or user_want_to_find == "d":
        a = float(input("Enter Length of edge of cube, a: "))
        d = (math.sqrt(3) * a)
        print("Space Diagonal of Cube is, d: ", d)
    else:
        print("Enter Correct input.")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    