
#Area of Elipse
#a = distance of vertical axis from centre of ellipse
#b = distance of Horizontal axis from centre of ellipse
# Area of Ellipse = 𝜋ab.
# # Area of Ellipse = 𝜋ab. to find a, a = Area/(π*b)
# Area of Ellipse = 𝜋ab. To find b, b = Area/(π*a)

def ellipse_area():
    a = float(input("Enter length of Vertical axis from centre of ellipse. "))
    b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
    print("Area of Elipse", (π*a*b))    

def ellipse_VertAxis():
    Area = float(input("Enter Area of ellipse. "))
    b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
    a = Area/(π*b)
    print("Length of vertical axis from centre of ellipse. ", a)

def ellipse_HoriAxis():
    Area = float(input("Enter Area of ellipse. "))
    a = float(input("Enter length of Vertical axis from centre of ellipse. "))
    b = Area/(π*a)
    print("Length of vertical axis from centre of ellipse. ",b)



while True:
    π = 3.14
    user_want_to_find = input("Slect what to Find? [A or Area, a, b]. ")
    if user_want_to_find == "A" or user_want_to_find == "Area":
        ellipse_area()

    elif user_want_to_find == "a":
        ellipse_VertAxis()

    elif user_want_to_find == "b":
        ellipse_HoriAxis()
    else:
        print("Enter Correct input.")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break