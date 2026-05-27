"""
docstring
"""
from shape import Shape
class Square(Shape):
    def __init__(self, shape_id, rid_length):
        """
        docstring
        :param shape_id:
        :param rid_length:
        """
        super().__init__(shape_id, shape_type="square")
        self.rid_length=rid_length

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
        dicti = {"id": 0, "type": "shape type", "length": self.rid_length}
        pass
