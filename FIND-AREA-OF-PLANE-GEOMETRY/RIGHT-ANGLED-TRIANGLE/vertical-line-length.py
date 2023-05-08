# Area of Right angled triangle
#A = Area, a = Horizontal line, b = base line of triangle.


while True:
    A = float(input("Enter Area of Triangle is A: " ))
    b = float(input("Enter base lin length of right angled Triangle a: "))
    print ("Verticle line length of right angled triangle is b: ", (2 * ( A / b)))

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break