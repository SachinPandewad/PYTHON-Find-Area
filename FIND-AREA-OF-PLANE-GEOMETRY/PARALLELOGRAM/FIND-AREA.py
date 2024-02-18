# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)

while True:
    b = float(input("Enter base lenght of parallelgrram: "))
    h = float(input("Enter height of Parallelogram: "))
    Aera = b * h
    print("Area of Parallelogram is ", Aera)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break