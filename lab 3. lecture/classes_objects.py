import math

class MyShape:
    def __init__(self, color="DefaultColor", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def getArea(self):
        return 0

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

class Rectangle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle - {super().__str__()}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}, Area: {self.getArea()}"

class Circle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle - {super().__str__()}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}, Area: {self.getArea()}"

color_input = input("Enter color for Rectangle: ")
filled_input = input("Is it filled? (Yes/No): ")
x_input = int(input("Enter X coordinate for Top Left corner: "))
y_input = int(input("Enter Y coordinate for Top Left corner: "))
length_input = int(input("Enter length of the rectangle: "))
width_input = int(input("Enter width of the rectangle: "))

rectangle = Rectangle(color_input, filled_input, x_input, y_input, length_input, width_input)

print(rectangle)
