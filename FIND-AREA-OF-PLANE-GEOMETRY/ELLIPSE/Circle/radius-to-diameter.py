

while True:

    user_function = input("What you want to find [radius or r, d or diameter] ")
    if user_function == "r" or user_function == "radius":
        d = float(input("Enter diameter."))
        print("daimeter is", (d /2)  )
    elif user_function == "diameter" or user_function == "d":
        r = float(input("Enter Radius."))
        print("daimeter is", r + r )
    else:
        print("Data Not Applicable")
    calculate = input("Want to find again? (y/n) : ")
    if calculate.lower() != "y":
        break