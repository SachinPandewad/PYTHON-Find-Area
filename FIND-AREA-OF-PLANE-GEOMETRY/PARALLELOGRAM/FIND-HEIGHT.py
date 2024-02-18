# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)

while True:
    A = float(input("Area of Parallelogram: "))
    b = float(input("Entar base of Parallelogram: "))
    h = (A / b)
    print("Height of Parallelogram is ", h)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break