#Area of Ractangle = width * length i.e. A = w * l
# w = width of Rectangle in cm.
# l = Length of Rectangle in cm.
# A = w * l, l = A / w.

while True:
    A = float(input("Enter Area of Rectangle in cm. "))
    w = float(input("Enter width of Rectangle in cm. "))
    l = (A / w)
    print("Length of Rectangle is ", l, "cm**2")

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break