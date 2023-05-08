# Cube
# A = Surface Area of Cube, a = Edge of cube
# d = space diagonal, V = volume
import math

while True:
    A = float(input("Enter Surface Area of Cube, A: "))
    a = (math.sqrt(A / 6))
    print("Length of edge of cube is, a: ", a)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    