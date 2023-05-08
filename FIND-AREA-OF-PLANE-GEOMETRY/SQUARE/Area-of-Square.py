# Area of Square = a**2
# a = length of one side of square

while True:
    a = float(input("Enter length of one side of square in cm"))
    Area = a**2
    print("Area of Square is : ", Area, "cm**2" )

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break