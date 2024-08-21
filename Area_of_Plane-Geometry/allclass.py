
π = 3.14
class Circle:
    

    def __init__(self):
        pass

    def circle_Area(self):
        user_function = input("Find-Area with [r, d] ")
        if user_function == "r":
            radius = float(input("Enter radius in cm. "))
            area_redi = ((radius**2) * (π))
            print("The Area of Circle with radius is ", area_redi, "cm**2" )

        elif user_function == "d" :
            self.diameter = float(input("Enter diameter in cm. "))
            area_dia = (((diameter // 2)**2) * π)
            print("The Area of Circle with diameter is", area_dia, "cm**2")

        else:
            print("Data Not Applicable") 

    def circle_circumferance(self):
        user_function = input("Find circumferance with [r, d] ")
        if user_function == "r":
            radius = float(input("Enter radius in cm. "))
            circum_redi= ((2) * (radius) * (π))
            print("The circumferance of Circle with radius is ", circum_redi, "cm**2" )

        elif user_function == "d" :
            diameter = float(input("Enter diameter in cm. "))
            circum_dia = (2 * (diameter / 2) * π)
            print("The circumferance of Circle with diameter is", circum_dia, "cm**2")

        else:
            print("Data Not Applicable")

    def circle_radius(self):
        user_function = input("Find-Radius with [A or Area, d or diameter] ")
        if user_function == "A" or user_function == "Area":
            area = float(input("Enter area of circle. "))
            redius_area = (math.sqrt((area)/(π)))
            print("Radius of circle is. ", redius_area )

        elif user_function == "d" or user_function == "diameter":
            diameter = float(input("Enter diameter of circle. "))
            redius_dia = (diameter / 2)
            print("Radius of circle is ", redius_dia)

        else:
            print("Data Not Applicable")

    def circle_diameter(self):
        user_function = input("Find-Daimeter with [A or Area, r or radius] ")
        if user_function == "Area" or user_function == "A":
            area = float(input("Enter area of circle. "))
            diameter_area= ((4 * area) / (π))
            print("Diameter of circle is. ", diameter_area )

        elif user_function == "radius" or user_function == "r":
            sradius = float(input("Enter Radius."))
            diameter_redi = (r * 2)
            print("diameter is", diameter_redi)

        else:
            print("Data Not Applicable")


class Ellipse:

    def __init__(self):
        pass
    
    def ellipse_area(self):
        lenVerticalAxis = float(input("Enter length of Vertical axis from centre of ellipse. "))
        lenHorizontalAxis= float(input("Enter length of Horizontal  axis from centre of ellipse. "))
        print("Area of Elipse", (π*lenVerticalAxis*lenHorizontalAxis))    

    def ellipse_VertAxis(self):
        Area = float(input("Enter Area of ellipse. "))
        b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
        a = Area/(π*b)
        print("Length of vertical axis from centre of ellipse. ", a)

    def ellipse_HoriAxis(self):
        Area = float(input("Enter Area of ellipse. "))
        a = float(input("Enter length of Vertical axis from centre of ellipse. "))
        b = Area/(π*a)
        print("Length of vertical axis from centre of ellipse. ",b)

class Parallelogram:
    
    def __init__(self):
        pass

    def parallelogram_Area(self):
        b = float(input("Enter base lenght of parallelgrram: "))
        h = float(input("Enter height of Parallelogram: "))
        Aera = b * h
        print("Area of Parallelogram is ", Aera)


    def parallelgrram_base(self):
        A = float(input("Area of Parallelogram: "))
        h = float(input("Entar height of Parallelogram: "))
        b = (A / h)
        print("Length of Base of Parallelogram is ", b)

    def parallelgrram_height(self):
        A = float(input("Area of Parallelogram: "))
        b = float(input("Entar base of Parallelogram: "))
        h = (A / b)
        print("Length of Height of Parallelogram is ", h)

    def parallelgrram_perimeter(self):
        a = float(input("Enter side length of Parallelogram: "))
        b = float(input("Enter base length of Paralleloigram: "))
        P = (2 * (a + b))
        print("Perimeter of Parallelogram: ", P)


    def parallelgrram_SideLength(self):
        P = float(input("Enter perimeter of Parallelogram: "))
        b = float(input("Enter base of Parallelogram: "))
        a = ((P / 2) - b)
        print("Side of Parallelogram, a: ", a)

class Rectangle:

    def __init__(self):
        pass

    def rectangle_Area(self):
        w = float(input("Enter width of Rectangle in cm. "))
        l = float(input("Enter Length of Rectangle in cm. "))
        A = (w * l)
        print("Area of Rectangle is ", A, "cm**2")

    def rectangle_width(self):
            A = float(input("Enter Area of Rectangle in cm. "))
            l = float(input("Enter Length of Rectangle in cm. "))
            w = (A / l)
            print("width of Rectangle is ", w, "cm**2")


    def rectangle_length(self):
            A = float(input("Enter Area of Rectangle in cm. "))
            w = float(input("Enter width of Rectangle in cm. "))
            l = (A / w)
            print("Length of Rectangle is ", l, "cm**2")

class Square:

    def __init__(self):
        pass
    
    def square_Area(self):
        a = float(input("Enter length of one side of square in cm : "))
        Area = a**2
        print("Area of Square is : ", Area, "cm**2" )

    def square_diagonal(self):
        a = float(input("Enter length of one side of square in cm : "))
        Diagonal = ((math.sqrt(2)) * (a))
        print("Diagonal of square is : ", Diagonal)

    def square_perimeter(self):        
        a = float(input("Enter length of one side of square in cm : "))
        Perimeter = (4) * (a)
        print("Area of Square is : ", Perimeter, "cm**2" )

    def square_side(self):
        user_choice = input("Find length of side of Square by [Area or A, Diagonal or D, Perimeter or P]")
        if user_choice == "Area" or user_choice == "A":
            Area = float(input("Enter Area of square in cm**2 : "))
            a = (math.sqrt(Area))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "Diagonal" or user_choice == "D":
            Diagonal = float(input("Enter length of diagonal in cm : "))
            a = (d) / (math.sqrt(2))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "Perimeter" or user_choice == "P":
            Perimeter = float(input("Enter Perimeter : "))
            a = (Perimeter / 4)
            print("length of one side of Square is : ", a, "cm")

class Triangle:
    def __init__(self):
        pass
    
    def triangle_Area (self):
        hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
        b =  float(input("Enter lenght of  base. b: "))
        A = ((hb * b) / 2)
        print("Area of Triangle is, A: ", A)

    def triangle_Perimeter(self):
            a = float(input("Enter length of side a: "))
            b = float(input("Enter lenght of  base. b: "))
            c = float(input("Enter length of side c: "))
            P = (a + b + c)
            print("Perimeter of Triangle is: ", P)

    def triangle_BaseLen(self):
            A = float(input("Enter Area of Triangle A: "))
            hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
            b = (2 * (A / hb))
            print(" Length of base is, b = ", b)

    def triangle_height(self):
            A = float(input("Enter Area of Triangle A: "))
            b =  float(input("Enter lenght of  base. b: "))
            hb =  (2 * (A / b))
            print("Height of triangle is, hb = ", hb)

    def triangle_SideALen(self):
            P = float(input("Enter Perimeter P: "))
            b = float(input("Enter lenght of  base. b: "))
            c = float(input("Enter length of side c: "))
            a = (P - b - c)
            print("Lenght of side a is: ", a)

    def triangle_SideCLen(self):
            P = float(input("Enter Perimeter P: "))
            a = float(input("Enter length of side a: "))
            b = float(input("Enter lenght of  base. b: "))
            c = (P - a - b)
            print("length of side c is: ", c)

