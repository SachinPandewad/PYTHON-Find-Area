#Area of Ractangle = width * length i.e. A = w * l
# w = width of Rectangle in cm.
# l = Length of Rectangle in cm.
# A = w * l, w = A / l.
# A = w * l, l = A / w.

while True:
    user_want_to_find = input("Slect what to Find? [A or Area, w, l] :")
    if user_want_to_find == "Area" or user_want_to_find == "A":
        w = float(input("Enter width of Rectangle in cm. "))
        l = float(input("Enter Length of Rectangle in cm. "))
        A = (w * l)
        print("Area of Rectangle is ", A, "cm**2")
    elif user_want_to_find == "w":
        A = float(input("Enter Area of Rectangle in cm. "))
        l = float(input("Enter Length of Rectangle in cm. "))
        w = (A / l)
        print("width of Rectangle is ", w, "cm**2")
    elif user_want_to_find == "l":
        A = float(input("Enter Area of Rectangle in cm. "))
        w = float(input("Enter width of Rectangle in cm. "))
        l = (A / w)
        print("Length of Rectangle is ", l, "cm**2")
    else:
        print("Enter Correct input.")
        
        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break