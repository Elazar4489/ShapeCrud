"""
docstring
"""
from shape import Shape


class Circle(Shape):
    def __init__(self, shape_id, radius):
        """
        docstring
        :param shape_id:
        :param radius:
        """
        super().__init__(shape_id, shape_type="square")
        self.radius = radius

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
        dicti = {"id": 0, "type": "shape type", "radius": self.radius}
        pass
