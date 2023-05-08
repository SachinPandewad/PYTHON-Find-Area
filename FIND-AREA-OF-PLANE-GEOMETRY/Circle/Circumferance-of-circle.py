# To Find circumferance, C = 2*π*r
#where π = 3.14, r = radius 
# if daimeter is given then daimer / 2 = radius

while True:
    user_function = input("Find-Area with [r, d] ")
    π = 3.14

    if user_function == "r":
        r = float(input("Enter radius in cm. "))
        print("The circumferance of Circle with radius is ", 2 * r * π, "cm**2" )
    elif user_function == "d" :
        d = float(input("Enter daimeter in cm. "))
        print("The circumferance of Circle with daimeter is", (2 * (d // 2) * π), "cm**2")
    else:
        print("Data Not Applicable")

    find_again = input("do you want to find circumferance again? (y/n): ")
    if find_again.lower() != "y":
        break