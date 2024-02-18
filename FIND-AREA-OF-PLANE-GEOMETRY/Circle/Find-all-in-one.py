# Import math Library
import math  #for square root


while True:
    π = 3.14
    user_want_to_find = input("what you want to find?  [A or Area, C or Circunferance, r or radius, d or diameter]")
    if user_want_to_find == "Area" or user_want_to_find ==  "A":
        user_function = input("Find-Area with [r, d] ")
        if user_function == "r":
            r = float(input("Enter radius in cm. "))
            print("The Area of Circle with radius is ", ((r**2) * (π)), "cm**2" )
        elif user_function == "d" :
            d = float(input("Enter diameter in cm. "))
            print("The Area of Circle with diameter is", (((d // 2)**2) * π), "cm**2")
        else:
            print("Data Not Applicable")    
    elif user_want_to_find == "Circumferance" or user_want_to_find == "C":
        user_function = input("Find-Area with [r, d] ")
        if user_function == "r":
            r = float(input("Enter radius in cm. "))
            print("The circumferance of Circle with radius is ", ((2) * (r) * (π)), "cm**2" )
        elif user_function == "d" :
            d = float(input("Enter diameter in cm. "))
            print("The circumferance of Circle with diameter is", (2 * (d / 2) * π), "cm**2")
        else:
            print("Data Not Applicable")
    elif user_want_to_find == "radius" or user_want_to_find == "r":
        user_function = input("Find-Radius with [A or Area, d or diameter] ")
        if user_function == "A" or user_function == "Area":
            area = float(input("Enter area of circle. "))
            print("Radius of circle is. ", (math.sqrt((area)/(π))) )
        elif user_function == "d" or user_function == "diameter":
            d = float(input("Enter diameter of circle. "))
            print("Radius of circle is ", (d / 2))
        else:
            print("Data Not Applicable")
    elif user_want_to_find == "diameter" or user_want_to_find == "d":
        user_function = input("Find-Daimeter with [A or Area, r or radius] ")
        if user_function == "Area" or user_function == "A":
            area = float(input("Enter area of circle. "))
            print("Diameter of circle is. ", ((4 * area) / (π)) )
        elif user_function == "radius" or user_function == "r":
            r = float(input("Enter Radius."))
            print("diameter is", (r + r) )
        else:
            print("Data Not Applicable")
    else:
        print("Data Not Applicable")

    calculate = input("Want to find again? (y/n) : ")
    if calculate.lower() != "y":
        break