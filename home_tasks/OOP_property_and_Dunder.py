class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("width must be greater than 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("height must be greater than 0")
        else:
            self.__height = value

    def __str__(self):
        return f"Прямоугольник {self.__width}x{self.__height}"

    def __add__(self, other):
        return (self.__width * self.__height) + (other.__width * other.__height)

rect1 = Rectangle(5, 4)
rect2 = Rectangle(10, 2)

print(rect1)
print(rect1 + rect2)

rect1.width = -5
