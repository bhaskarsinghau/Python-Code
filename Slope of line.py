# Line slope
def calc():
    x, y = input("Enter x and y coordinates: ").split()
    x2, y2 = input("Enter the second x and y coordinates: ").split()
    ys = int(y2) - int(y)
    xs = int(x2) - int(x)
    result = int(ys) / int(xs)
    print("The Slope of line is :",result)
calc()

