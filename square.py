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
        return self.rid_length*self.rid_length

    def get_perimeter(self):
        """
        docstring
        :return:
        """
        return self.rid_length*4

    def to_dict(self):
        """
        docstring
        :return:
        """
        dicti = {"id": self.shape_id, "type": self.shape_type, "length": self.rid_length}
        # TO DO
        return dicti
