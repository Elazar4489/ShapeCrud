"""
docstring
"""
from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id: int, sizes: dict):
        """
        docstring
        :param shape_id:
        :param length:
        :param width:
        """
        super().__init__(shape_id, shape_type="rectangle")
        self.length = int(sizes["length"])
        self.width=int(sizes["width"])

    def get_area(self):
        """
        docstring
        :return:
        """
        return self.length * self.width

    def get_perimeter(self):
        """
        docstring
        :return:
        """
        return (self.length+self.width) *2

    def to_dict(self):
        """
        docstring
        :return:
        """
        dicti = {"id": self.shape_id, "type": self.shape_type, "length": self.length, "width": self.width}
        return dicti
