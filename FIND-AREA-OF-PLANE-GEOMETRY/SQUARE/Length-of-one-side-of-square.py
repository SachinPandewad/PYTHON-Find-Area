# Area of Square = a**2
# a = length of one side of square
#A = a**2, a = (math.sqrt(Area))

import math 

while True:
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