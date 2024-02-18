# Cube
# A = Surface Area of Cube, a = Edge of cube
# d = space diagonal, V = volume

while True:
    a = float(input("Enter Length of edge of cube, a: "))
    V = (a**3)
    print("Volume of Cube is, V: ", V)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break