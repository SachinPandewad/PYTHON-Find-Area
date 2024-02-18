# Area of Circle
# A = πr**2
# π = 3.14,  r = radius , d = daimeter

while True:
    user_function = input("Find-Area with [r, d] ")
    π = 3.14

    if user_function == "r":
        r = float(input("Enter radius in cm. "))
        print("The Area of Circle with radius is ", ((r**2) * π), "cm**2" )
    elif user_function == "d" :
        d = float(input("Enter daimeter in cm. "))
        print("The Area of Circle with daimeter is", (((d // 2)**2) * π), "cm**2")
    else:
        print("Data Not Applicable")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break