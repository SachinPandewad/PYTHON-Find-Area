# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)
# Perimeter = P, a = side length

while True:
    P = float(input("Enter perimeter of Parallelogram: "))
    b = float(input("Enter base of Parallelogram: "))
    a = ((P / 2) - b)
    print("Side of Parallelogram, a: ", a)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break