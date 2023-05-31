import figure
myline = figure.line(10, 20)

width, heigth = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, heigth)
    print(rectangle)
except ValueError:
    print("please input positive number for width and heigth")
