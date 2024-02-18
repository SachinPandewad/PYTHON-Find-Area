#Area of Elipse
#a = Length of vertical axis from centre of ellipse.
#b = Length of Horizontal axis from centre of ellipse.
# Area of Ellipse = 𝜋ab. To find b, b = Area/(π*a)

while True:
    π = 3.14
    Area = float(input("Enter Area of ellipse. "))
    a = float(input("Enter length of Vertical axis from centre of ellipse. "))
    b = Area/(π*a)
    print(b)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break