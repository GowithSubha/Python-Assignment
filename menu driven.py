# Write a menu-driven python program that calculates Circumference and Area of different shapes using function.
def rectangle_area():
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breadth of the rectangle: "))
    area = l*b
    print("Area of rectangle is: ", area)
    
def rectangle_circumference():
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breadth of the rectangle: "))
    circumference = 2*(l+b)
    print("Circumference of rectangle is: ", circumference)
    
def circle_area():
    r = int(input("Enter the radius of the circle: "))
    area = 3.14*r*r
    print("Area of circle is: ", area)
    
def circle_circumference():
    r = int(input("Enter the radius of the circle: "))
    circumference = 2*3.14*r
    print("Circumference of circle is: ", circumference)
    
def square_area():
    s = int(input("Enter the side of the square: "))
    area = s*s
    print("Area of square is: ", area)
    
def square_circumference():
    s = int(input("Enter the side of the square: "))
    circumference = 4*s
    print("Circumference of square is: ", circumference)
    
def triangle_area():
    b = int(input("Enter the base of the triangle: "))
    h = int(input("Enter the height of the triangle: "))
    area = 0.5*b*h
    print("Area of triangle is: ", area)
    
def triangle_circumference():
    a = int(input("Enter the first side of the triangle: "))
    b = int(input("Enter the second side of the triangle: "))
    c = int(input("Enter the third side of the triangle: "))
    circumference = a+b+c
    print("Circumference of triangle is: ", circumference)
    
def parallelogram_area():
    b = int(input("Enter the base of the parallelogram: "))
    h = int(input("Enter the height of the parallelogram: "))
    area = b*h
    print("Area of parallelogram is: ", area)
    
def parallelogram_circumference():
    a = int(input("Enter the first side of the parallelogram: "))
    b = int(input("Enter the second side of the parallelogram: "))
    circumference = 2*(a+b)
    print("Circumference of parallelogram is: ", circumference)
    
print("MENU")
print("What do you want to calculate?")
print("1: Area")
print("2: Circumference")
print("3: Exit")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("What shape do you want to calculate area of?")
    print("1: Rectangle")
    print("2: Circle")
    print("3: Square")
    print("4: Triangle")
    print("5: Parallelogram")
    shape = int(input("Enter your choice: "))
    if shape == 1:
        rectangle_area()
    elif shape == 2:
        circle_area()
    elif shape == 3:
        square_area()
    elif shape == 4:
        triangle_area()
    elif shape == 5:
        parallelogram_area()
    else:
        print("Invalid choice!")
        
elif choice == 2:
    print("What shape do you want to calculate circumference of?")
    print("1: Rectangle")
    print("2: Circle")
    print("3: Square")
    print("4: Triangle")
    print("5: Parallelogram")
    shape = int(input("Enter your choice: "))
    if shape == 1:
        rectangle_circumference()
    elif shape == 2:
        circle_circumference()
    elif shape == 3:
        square_circumference()
    elif shape == 4:
        triangle_circumference()
    elif shape == 5:
        parallelogram_circumference()
    else:
        print("Invalid choice!")
        
elif choice == 3:
    print("Thank you!")
    
else:
    print("Invalid choice!")
    
