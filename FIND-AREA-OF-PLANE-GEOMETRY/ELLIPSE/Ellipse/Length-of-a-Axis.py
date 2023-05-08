#Area of Elipse
#a = Length of vertical axis from centre of ellipse.
#b = Length of Horizontal axis from centre of ellipse.
# Area of Ellipse = 𝜋ab. to find a, a = Area/(π*b).

while True:
    π = 3.14
    Area = float(input("Enter Area of ellipse. "))
    b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
    a = Area/(π*b)
    print("Length of vertical axis from centre of ellipse. ", a)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break