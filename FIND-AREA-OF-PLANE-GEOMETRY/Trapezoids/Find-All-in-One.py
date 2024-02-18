#Area of Trapezoid
# a= upper base, b = lower base, h = Height (perpendicular line to base)
# Perimeter = P, c = side c(right), d = side d(left)

while True:
    User_want_to_find = input("Select what to find: [upper base or a, b or lower base, h or Height, Perimeter or P, c or side c(right), d or side d(left)]")

    if User_want_to_find =="upper base" or User_want_to_find == "a":
        A = float(input("Area of Trapezoid is: "))
        b = float(input("Length of Lower base: "))
        h = float(input("Length of Hieght: "))
        a = ((2 * (A / h)) -b )
        print("Length of upper base: ", a)
    elif User_want_to_find == "lower base" or User_want_to_find == "b":
        A = float(input("Area of Trapezoid is: "))
        a = float(input("Length of upper base: "))
        h = float(input("Length of Hieght: "))
        b = ((2 * (A / h)) - a)
        print("Length of Lower base: ", b)
    elif User_want_to_find == "Height" or User_want_to_find == "h":
        A = float(input("Area of Trapezoid is: "))
        a = float(input("Length of upper base: "))
        b = float(input("Length of Lower base: "))
        h = (2 * (A / ( a + b)))
        print("Length of Hieght: ", h)
    elif User_want_to_find == "Perimeter" or User_want_to_find == "P":
        a = float(input("Length of upper base: "))
        b = float(input("Length of Lower base: "))
        c = float(input("Length of side c(right): "))
        d = float(input("Length of side d(left): "))
        P = (a + b + c + d)
        print("Perimeter of trapezoid: ", P)
    elif User_want_to_find ==  "side c" or User_want_to_find == "c":
        P = float(input("Perimeter of trapezoid: "))
        a = float(input("Length of upper base: "))
        b = float(input("Length of Lower base: "))
        d = float(input("Length of side d(left): "))
        c = (a + b + P + d)
        print("Length of side c(right): ", c)
    elif User_want_to_find == "side d" or User_want_to_find == "d":
        P = float(input("Perimeter of trapezoid: "))
        a = float(input("Length of upper base: "))
        b = float(input("Length of Lower base: "))
        c = float(input("Length of side c(right): "))
        d = (P - a - b - c)
        print("Length of side d(left): ", d)
    else:
        print("Enter Correct input.")
        
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break