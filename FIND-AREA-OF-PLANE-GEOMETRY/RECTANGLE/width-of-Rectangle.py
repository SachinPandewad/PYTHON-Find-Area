#Area of Ractangle = width * length i.e. A = w * l
# w = width of Rectangle in cm.
# l = Length of Rectangle in cm.
# A = w * l, w = A / l

while True:
    A = float(input("Enter Area of Rectangle in cm. "))
    l = float(input("Enter Length of Rectangle in cm. "))
    w = (A / l)
    print("width of Rectangle is ", w, "cm**2")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break