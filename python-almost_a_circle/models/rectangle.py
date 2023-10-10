#!/usr/bin/python3
"""
    Class Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.

    Attrs:
        width (int)
        height (int)
        x (int)
        y (int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class.

        Args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)
        """
        self.w_valid(width)
        self.h_valid(height)
        self.x_valid(x)
        self.y_valid(y)      
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """w getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """w setter"""
        self.w_valid(value)
        self.__width = value

    @property
    def height(self):
        """h getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """h setter"""
        self.h_valid(value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.x_valid(x)
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.y_valid(y)
        self.__y = y

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def display(self):
        """Return rectangle area."""
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
        """Return rectangle area."""
        if not isinstance(arg, int):
            raise TypeError("width must be an integer")
        if arg <= 0:
            raise ValueError("width must be > 0")

    @staticmethod
    def h_valid(arg):
        """Return rectangle area."""
        if not isinstance(arg, int):
            raise TypeError("height must be an integer")
        if arg <= 0:
            raise ValueError("height must be > 0")

    @staticmethod
    def x_valid(arg):
        """Return rectangle area."""
        if not isinstance(arg, int):
            raise TypeError("x must be an integer")
        if arg < 0:
            raise ValueError("x must be >= 0")

    @staticmethod
    def y_valid(arg):
        """Return rectangle area."""
        if not isinstance(arg, int):
            raise TypeError("y must be an integer")
        if arg < 0:
            raise ValueError("y must be >= 0")
