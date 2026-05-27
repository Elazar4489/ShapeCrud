"""
docstring
"""
from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, length, width):
        """
        docstring
        :param shape_id:
        :param length:
        :param width:
        """
        super().__init__(shape_id, shape_type="square")
        self.length = length
        self.width=width

    def get_area(self):
        """
        docstring
        :return:
        """
        pass

    def get_perimeter(self):
        """
        docstring
        :return:
        """
        pass

    def to_dict(self):
        """
        docstring
        :return:
        """
        dicti = {"id": 0, "type": "shape type", "length": self.length, "width": self.width}
        pass
