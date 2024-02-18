# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)
# Perimeter = P, a = side length

while True:
    a = float(input("Enter side length of Parallelogram: "))
    b = float(input("Enter base length of Paralleloigram: "))
    P = (2 * (a + b))
    print("Perimeter of Parallelogram: ", P)
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break