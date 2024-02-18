# Cube
# A = Surface Area of Cube, a = Edge of cube
# d = space diagonal, V = volume

while True:
    a = float(input("Enter Length of edge of cube, a: "))
    A = (6 * (a**2))
    print("Surface area of Cube is, A = ", A)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    