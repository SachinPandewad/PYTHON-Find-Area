# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)

while True:
    A = float(input("Area of Parallelogram: "))
    h = float(input("Entar height of Parallelogram: "))
    b = (A / h)
    print("Base of Parallelogram is ", b)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break