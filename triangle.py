def triangle ():
    hyp =int(input("Enter length of first side:"))
    base =int(input("Enter length of second side:"))
    height =int(input("Enter length of third side:"))
    if hyp*hyp == (base*base)+(height*height):
        print("The given triangle is a right triangle.")
    else:
        print("The given triangle is not a right triangle.")
triangle()