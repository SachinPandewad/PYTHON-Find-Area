#Area of Ractangle = width * length i.e. A = w * l
# w = width of Rectangle in cm.
# l = Length of Rectangle in cm.


while True:
    w = float(input("Enter width of Rectangle in cm. "))
    l = float(input("Enter Length of Rectangle in cm. "))
    A = (w * l)
    print("Area of Rectangle is ", A, "cm**2")
    
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break