"""
docstring
"""
from shape import Shape
from math import pi, pow


class Circle(Shape):
    def __init__(self, shape_id, radius):
        """
        docstring
        :param shape_id:
        :param radius:
        """
        super().__init__(shape_id, shape_type="circle")
        self.radius = radius

    def get_area(self):
        """
        docstring
        :return:
        """
        return pow(self.radius, 2) * pi


    def get_perimeter(self):
        """
        docstring
        :return:
        """
        return self.radius * 2 * pi


    def to_dict(self):
        """
        docstring
        :return:
        """
        dicti = {"id": self.shape_id, "type": self.shape_type, "radius": self.radius}
        return dicti

