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
        """se"""
        s = f"[Rectangle] ({self.id}) {self.__x}"
        t = f"/{self.__y} - {self.__width}/{self.__height}"
        return s + t

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
        for _ in range(self.__height):
            for _ in range(1, self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ddsds"""
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "width":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """dds"""
        new_dic = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
        return new_dic

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
