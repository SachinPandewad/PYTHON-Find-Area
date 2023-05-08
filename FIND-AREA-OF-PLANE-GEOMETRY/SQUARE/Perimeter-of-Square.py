# Perimeter is a line joinig to opposite corner points of a square
# Perimeter of square = P = 4a
# a = length of one side of square

while True:
    a = float(input("Enter length of one side of square in cm "))
    Perimeter = (4) * (a)
    print("Area of Square is : ", Perimeter, "cm**2" )

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break