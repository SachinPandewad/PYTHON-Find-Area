# Area of Right angled triangle
#A = Area, a = vertical line, b = base line of triangle.

while True:
    A = float(input("Enter Area of Triangle is A: " ))
    a = float(input("Enter verticle side of right angled Triangle a: "))
    print ("base line length of right angled triangle is b: ", (2 * ( A / a)))

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break    