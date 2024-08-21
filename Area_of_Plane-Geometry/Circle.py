# Here we can find all parameters of the circle in dimple way.
import math  #for square root




def circle_Area():
    user_function = input("Find-Area with [r, d] ")
    if user_function == "r":
        r = float(input("Enter radius in cm. "))
        area_redi = ((r**2) * (π))
        print("The Area of Circle with radius is ", area_redi, "cm**2" )

    elif user_function == "d" :
        d = float(input("Enter diameter in cm. "))
        area_dia = (((d // 2)**2) * π)
        print("The Area of Circle with diameter is", area_dia, "cm**2")

    else:
        print("Data Not Applicable") 

def circle_circumferance():
    user_function = input("Find circumferance with [r, d] ")
    if user_function == "r":
        r = float(input("Enter radius in cm. "))
        circum_redi= ((2) * (r) * (π))
        print("The circumferance of Circle with radius is ", circum_redi, "cm**2" )

    elif user_function == "d" :
        d = float(input("Enter diameter in cm. "))
        circum_dia = (2 * (d / 2) * π)
        print("The circumferance of Circle with diameter is", circum_dia, "cm**2")

    else:
        print("Data Not Applicable")

def circle_radius():
    user_function = input("Find-Radius with [A or Area, d or diameter] ")
    if user_function == "A" or user_function == "Area":
        area = float(input("Enter area of circle. "))
        redius_area = (math.sqrt((area)/(π)))
        print("Radius of circle is. ", redius_area )

    elif user_function == "d" or user_function == "diameter":
        d = float(input("Enter diameter of circle. "))
        redius_dia = (d / 2)
        print("Radius of circle is ", redius_dia)

    else:
        print("Data Not Applicable")

def circle_diameter():
    user_function = input("Find-Daimeter with [A or Area, r or radius] ")
    if user_function == "Area" or user_function == "A":
        area = float(input("Enter area of circle. "))
        diameter_area= ((4 * area) / (π))
        print("Diameter of circle is. ", diameter_area )

    elif user_function == "radius" or user_function == "r":
        r = float(input("Enter Radius."))
        diameter_redi = (r * 2)
        print("diameter is", diameter_redi)

    else:
        print("Data Not Applicable")



    while True:
        π = 3.14 # You can write 'π' with pressing "Alt+227" and release alt button 
        user_want_to_find = input("what you want to find?  [A or Area, C or Circunferance, r or radius, d or diameter]")
        # User has to type any one input to find what h want to find
        if user_want_to_find == "Area" or user_want_to_find ==  "A":
            circle_Area()
        elif user_want_to_find == "Circumferance" or user_want_to_find == "C":
            circle_circumferance()
        elif user_want_to_find == "radius" or user_want_to_find == "r":
            circle_radius()
        elif user_want_to_find == "diameter" or user_want_to_find == "d":
            circle_diameter()
        else:
            print("Data Not Applicable")

        calculate = input("Want to find again? (y/n) : ")
        if calculate.lower() != "y":
            break



        