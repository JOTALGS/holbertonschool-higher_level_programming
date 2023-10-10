#!/usr/bin/python3
"""eerer"""

from base import Base


class Rectangle(Base):
    """sdsdsd"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ini"""
        self.w_valid(width)
        self.h_valid(height)
        self.x_valid(x)
        self.y_valid(y)      
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.w_valid(value)
        self.__width = value

    @property
    def height(self):
        """h getter"""
        return self.__height

    @height.setter
    def height(self, value):
        self.h_valid(value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.x_valid(x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.y_valid(y)
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__y):
            print()
        stri = ""
        if self.__width == 0 or self.__height == 0:
            print(stri)
        else:
            for i in range(self.__height):
                for _ in range(1, self.__x):
                    stri += " "
                for _ in range(self.__width):
                    stri += "#"
                if i != self.__height - 1:
                    stri += "\n"
            print(stri)

    @staticmethod
    def w_valid(arg):
        if not isinstance(arg, int):
            raise TypeError("width must be an integer")
        if arg <= 0:
            raise ValueError("width must be > 0")

    @staticmethod
    def h_valid(arg):
        if not isinstance(arg, int):
            raise TypeError("height must be an integer")
        if arg <= 0:
            raise ValueError("height must be > 0")

    @staticmethod
    def x_valid(arg):
        if not isinstance(arg, int):
            raise TypeError("x must be an integer")
        if arg < 0:
            raise ValueError("x must be >= 0")

    @staticmethod
    def y_valid(arg):
        if not isinstance(arg, int):
            raise TypeError("y must be an integer")
        if arg < 0:
            raise ValueError("y must be >= 0")
