# Area of Parallelogram
# A= Area, b = base, h= height(perpendicular to base)
# Perimeter = P, a = side length

while True:
    User_want_to_find = input("Select what to find? [Area or A, base or b, height of h, Perimeter or P, side length or a ]")

    if User_want_to_find == "Area" or User_want_to_find == "A":
        b = float(input("Enter base lenght of parallelgrram: "))
        h = float(input("Enter height of Parallelogram: "))
        Aera = b * h
        print("Area of Parallelogram is ", Aera)
    elif User_want_to_find == "base" or User_want_to_find == "b":
        A = float(input("Area of Parallelogram: "))
        h = float(input("Entar height of Parallelogram: "))
        b = (A / h)
        print("Base of Parallelogram is ", b)
    elif User_want_to_find == "height" or User_want_to_find == "h":
        A = float(input("Area of Parallelogram: "))
        b = float(input("Entar base of Parallelogram: "))
        h = (A / b)
        print("Height of Parallelogram is ", h)
    elif User_want_to_find == "perineter" or User_want_to_find == "P":
        a = float(input("Enter side length of Parallelogram: "))
        b = float(input("Enter base length of Paralleloigram: "))
        P = (2 * (a + b))
        print("Perimeter of Parallelogram: ", P)
    elif User_want_to_find == "side length" or User_want_to_find == "a":
        P = float(input("Enter perimeter of Parallelogram: "))
        b = float(input("Enter base of Parallelogram: "))
        a = ((P / 2) - b)
        print("Side of Parallelogram, a: ", a)
    else:
        print("Enter Correct input.")
        
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break