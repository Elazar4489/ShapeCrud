"""
docstring
"""
from shape import Shape
class Square(Shape):
    def __init__(self, shape_id: int, sizes: dict):
        """
        docstring
        :param shape_id:
        :param rid_length:
        """
        super().__init__(shape_id, shape_type="square")
        self.length=int(sizes["length"])

    def get_area(self):
        """
        docstring
        :return:
        """
        return self.length*self.length

    def get_perimeter(self):
        """
        docstring
        :return:
        """
        return self.length*4

    def to_dict(self):
        """
        docstring
        :return:
        """
        dicti = {"id": self.shape_id, "type": self.shape_type, "length": self.length}
        # TO DO
        return dicti
