#Area of Elipse
#a = distance of vertical axis from centre of ellipse
#b = distance of Horizontal axis from centre of ellipse
# Area of Ellipse = 𝜋ab

while True:
    𝜋=3.14
    a = float(input("Enter length of Vertical axis from centre of ellipse. "))
    b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
    print("Area of Elipse", (π*a*b))
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break