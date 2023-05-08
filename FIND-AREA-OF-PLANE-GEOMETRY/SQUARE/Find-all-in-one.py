# Area of Square = a**2
# a = length of one side of square
#Perimeter of square = P = 4a
#A = a**2, a = (math.sqrt(Area))

import math 

while True:
    user_want_to_find = input("Slect what to Find? [A or Area, Diagonal or D, Perimeter or P, side a or a ] :")
    if user_want_to_find == "Area" or  user_want_to_find == "A":
        a = float(input("Enter length of one side of square in cm : "))
        Area = a**2
        print("Area of Square is : ", Area, "cm**2" )
    elif user_want_to_find == "Diagonal" or user_want_to_find == "D":
        a = float(input("Enter length of one side of square in cm : "))
        Diagonal = ((math.sqrt(2)) * (a))
        print("Diagonal of square is : ", Diagonal)
    elif user_want_to_find == "Perimeter" or user_want_to_find == "P":
        a = float(input("Enter length of one side of square in cm : "))
        Perimeter = (4) * (a)
        print("Area of Square is : ", Perimeter, "cm**2" )
    elif user_want_to_find == "side a" or user_want_to_find == "a":
        user_choice = input("Find length of side of Square by [Area or A, Diagonal or D, Perimeter or P]")
        if user_choice == "Area" or user_choice == "A":
            Area = float(input("Enter Area of square in cm**2 : "))
            a = (math.sqrt(Area))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "Diagonal" or user_choice == "D":
            Diagonal = float(input("Enter length of diagonal in cm : "))
            a = (d) / (math.sqrt(2))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "Perimeter" or user_choice == "P":
            Perimeter = float(input("Enter Perimeter : "))
            a = (Perimeter / 4)
            print("length of one side of Square is : ", a, "cm")
    else:
        print("Enter Correct input.")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break