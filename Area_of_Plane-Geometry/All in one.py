from allclass import  Circle
from allclass import Ellipse
from allclass import Parallelogram
from allclass import Rectangle
from allclass import Square
from allclass import Triangle


while True:
    print("Solution of What Geometry You Want to Find? :")
    user_input = input("Circle or C, Ellipse or E, Parallelogram, Rectangle or R, Square or S, Triangle or T :")

    if user_input == "Circle" or user_input == 'C':
        ucircle=Circle()
        user_want_to_find = input("what you want to find?  [A or Area, C or Circunferance, r or radius, d or diameter]")
        if user_want_to_find == "Area" or user_want_to_find ==  "A":
            ucircle.circle_Area()
        elif user_want_to_find == "Circumferance" or user_want_to_find == "C":
            ucircle.circle_circumferance()
        elif user_want_to_find == "radius" or user_want_to_find == "r":
            ucircle.circle_radius()
        elif user_want_to_find == "diameter" or user_want_to_find == "d":
            ucircle.circle_diameter()
        else:
            print("Data Not Applicable")

    elif user_input == "Ellipse" or user_input == 'E':
        user_want_to_find = input("Slect what to Find? [A or Area, a, b]. ")
        uellipse = Ellipse()
        if user_want_to_find == "A" or user_want_to_find == "Area":
            uellipse.ellipse_area()
        elif user_want_to_find == "a":
            uellipse.ellipse_VertAxis()
        elif user_want_to_find == "b":
            uellipse.ellipse_HoriAxis()
        else:
            print("Enter Correct input.")

    
    elif user_input == 'Parallelogram' or user_input== 'P':
        User_want_to_find = input("Select what to find? [Area or A, base or b, height of h, Perimeter or P, side length or a ]")
        
        if User_want_to_find == "Area" or User_want_to_find == "A":
            uparallelogram=parallelogram_Area()
        elif User_want_to_find == "base" or User_want_to_find == "b":
            uparallelogram.parallelgrram_base()
        elif User_want_to_find == "height" or User_want_to_find == "h":
            uparallelogram.parallelgrram_height()
        elif User_want_to_find == "perimeter" or User_want_to_find == "P":
            uparallelogram.parallelgrram_perimeter()
        elif User_want_to_find == "side length" or User_want_to_find == "a":
            uparallelogram.parallelgrram_SideLength()
        else:
            print("Enter Correct input.")

    elif user_input== 'Rectangle' or user_input=='R':
        user_want_to_find = input("Slect what to Find? [A or Area, w, l] :")
        urectangle= Rectangle()
        if user_want_to_find == "Area" or user_want_to_find == "A":
            urectangle.rectangle_Area()
        elif user_want_to_find == "w":
            urectangle.rectangle_width()
        elif user_want_to_find == "l":
            urectangle.rectangle_length()
        else:
            print("Data is not aplicable..! Please Enter Correct Input.")
    
    elif user_input== "Square" or user_input=='S':
        user_want_to_find = input("Slect what to Find? [A or Area, Diagonal or D, Perimeter or P, side a or a ] :")
        usquare = Square()
        if user_want_to_find == "Area" or  user_want_to_find == "A":
            usquare.square_Area()
        elif user_want_to_find == "Diagonal" or user_want_to_find == "D":
            usquare.square_diagonal()
        elif user_want_to_find == "Perimeter" or user_want_to_find == "P":
            usquare.square_perimeter()
        elif user_want_to_find == "side a" or user_want_to_find == "a":
            usquare.square_side()
        else:
            print("Enter Correct input.")

    elif user_input =='Triangle' or user_input=='T':
        user_want_to_find = input("Select what to find? [Area or A, Perimeter or P, base length or b, height or hb, length of side a or a, length of side c or c ]")
        utriangle = Triangle()
        if user_want_to_find == "Area" or user_want_to_find == "A":
            utriangle.triangle_Area()
        elif user_want_to_find == "Perimeter" or user_want_to_find == "P":
            utriangle.triangle_Perimeter()
        elif user_want_to_find == "base length" or  user_want_to_find == "b":
            utriangle.triangle_BaseLen()
        elif user_want_to_find == "Height" or user_want_to_find == "hb":
            utriangle.triangle_height()
        elif user_want_to_find == "length of side a " or user_want_to_find == "a":
            utriangle.triangle_SideALen()
        elif user_want_to_find == "length of side c" or user_want_to_find == "c":
            utriangle.triangle_SideCLen()
        else:
            print("Enter correct input.")
    else:
        print("Input doesn't match with given data. Please enter Valid input again..!")
        
    
    calculate = input("Want to find again? (y/n) : ")
    if calculate.lower() != "y":
        break


