#!/usr/bin/python3
"""
    Class Base.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """hbbsa"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ddsga  dgffghfhhhmbvbs"""
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """ sdbhhjverjhvre lbmhba """
        dic = self.__dict__
        new_dic = {}
        for key, value in dic.items():
            if key == 'id':
                new_dic[key] = value
            elif key == '_Rectangle__width':
                new_dic['size'] = value
            elif key == '_Rectangle__height':
                pass
            else:
                new_dic[key[12:]] = value
        return new_dic
