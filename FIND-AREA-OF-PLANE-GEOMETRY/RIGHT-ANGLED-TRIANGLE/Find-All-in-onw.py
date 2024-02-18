#A = Area, a = verticle line, b = base line of triangle.
#c = Hypotenuse, Perimeter = c
import math


while True:
    user_want_to_find = input("Select what to find? [Perimeter or c, Hypotenuse or c, A or Area, base lenght or b, Verticle line length or a]: ")

    if user_want_to_find == "A" or user_want_to_find == "Area":
        a = float(input("vertical Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Area of Right angled triangle is A: ", ((a * b) /  2))
    elif user_want_to_find == "base lenght" or user_want_to_find == "b":
        A = float(input("Enter Area of Triangle is A: " ))
        a = float(input("Enter verticle side of right angled Triangle a: "))
        print ("base line length of right angled triangle is b: ", (2 * ( A / a)))
    elif user_want_to_find == "Verticle line length" or user_want_to_find == "a":
        A = float(input("Enter Area of Triangle is A: " ))
        b = float(input("Enter base lin length of right angled Triangle a: "))
        print ("Verticle line length of right angled triangle is b: ", (2 * ( A / b)))
    elif user_want_to_find == "Hypotenuse" or user_want_to_find == "c":
        a = float(input("Verticle Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Length of Hypotenuse is ", math.sqrt((a**2) + (b**2)))
    elif user_want_to_find == "Perimeter" or user_want_to_find == "c":
        a = float(input("vertical Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Perimeter if Right Angled Triangle, P is ", (a + b) + (math.sqrt((a**2) + (b**2))) )
    else:
        print("Enter Correct input.")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break