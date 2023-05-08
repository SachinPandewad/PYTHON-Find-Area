# r = Radius to find, Pi = 3.14
# d = daimeter, A = Area,
# using area of circle = Pi *  
import math # for finding square root

while True:
    user_function = input("Find-Radius with [A or Area, d or diameter] ")
    π = 3.14
    if user_function == "A" or user_function == "Area":
        area = float(input("Enter area of circle. "))
        print("Radius of circle is. ", (math.sqrt((area)/(π))))
    elif user_function == "d" or user_function == "diameter":
        d = float(input("Enter diameter of circle. "))
        print("Radius of circle is ", ((d) / (2)) )
    else:
        print("Data Not Applicable")
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break