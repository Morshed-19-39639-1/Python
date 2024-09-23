

print("---Enter any operation (Triangle,Rectangle,Trapezoid,Ellipse,Square,Parallelogram,Circle, Circumference )-------")

operator = input("Enter operation : ")

base = float(input("Enter base in cm : "))
height = float(input("Enter Height in cm : "))
width = float(input("Enter Width in cm : "))
length = float(input("Enter Length in cm : "))
radius = float(input("Enter Radius in cm : "))


if operator == "Triangle":
    print("The area of Triangle is : ", 0.5 * base * height)
elif operator == "Rectangle":
    print("The area of Rectangle is : ", width * height)
elif operator == "Ellipse":
    print("The area of Ellipse is : ", 3.1416 * length * base)
elif operator == "Square":
    print("The area of Square value is : ", length * length)
elif operator == "Parallelogram":
    print("The area of Parallelogram is : ", base * height)
elif operator == "Circle":
    print("The area of Circle is : ", 3.1416 * radius * radius)
elif operator == "Circumference":
    print("The area of Circumference is : ", 6.2432 * radius)
else:
    print("Invalid Operation")
