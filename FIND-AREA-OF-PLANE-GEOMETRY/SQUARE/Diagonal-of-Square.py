# Diagonal of Square is D = (math.sqrt(2)) * (a)
# a = length of one side of square
import math

while True:
    a = float(input("Enter length of one side of square in cm "))
    Diagonal = ((math.sqrt(2)) * (a))
    print("Diagonal of square is : ", Diagonal)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break