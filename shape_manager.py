import os.path
from square import Square
from rectangle import Rectangle
from circle import Circle
import json
import logging

"""
ייבוא תיקיות מקומיות וספריות שימושיות לפרוייקט
"""


"""
יצירת לוגר
"""
logger = logging.getLogger("shape manager project")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("shapes_log.log", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""
מחלקה ראשית שמנהלת את הפרוייקט
"""
class ShapeManager:

#==========================================1==============================================#

    def __init__(self):
        """
        docstring
        פונקציית בנאי שמכילה שדה של רשימה ומפעילה באופן אוטומטי את פונקציית הטעינה מקובץ JSON לרשימה
        """
        self.shapes = []
        self.load_from_json()

#==========================================2==============================================#

    def create_shape(self, shape: dict):
        classes={
            "square": Square,
            "rectangle": Rectangle,
            "circle": Circle
        }
        the_type=shape["type"]
        shape_id=self.return_id()
        try:
            new_shape=classes[the_type](shape_id, shape)
        except KeyError:
            raise KeyError
        except ValueError:
            raise ValueError
        self.shapes.append(new_shape)
        return new_shape

# #==========================================3==============================================#

    def get_all_shapes(self):
        """
        docstring
        מציגה את כל הצורות (האובייקטים) שקיימות ברשימה
        :return: את הרשימה
        """
        return [shape.to_dict() for shape in self.shapes]

# #==========================================4==============================================#

    def update_shape(self, shape_id: int, new_data: dict):

        classes = {
            "square": Square,
            "rectangle": Rectangle,
            "circle": Circle
        }
        the_type = new_data["type"]
        try:
            new_shape = classes[the_type](shape_id, new_data)
        except KeyError:
            raise KeyError
        old_shape=self.return_object_by_id(shape_id)
        self.shapes[old_shape[1]]=new_shape
        return new_shape

# #==========================================5==============================================#

    def delete_shape(self, shape_id):
        """
        docstring
        :param shape_id:
        :return:
        """
        the_shape=self.return_object_by_id(shape_id)
        if not the_shape:
            raise KeyError
        self.shapes.remove(the_shape[0])
        return the_shape

# #==========================================6==============================================#
    def get_one_shape(self, shape_id):

        return self.return_object_by_id(shape_id)[0].to_dict()


    def get_sum_area(self):
        list_of_area_shapes=[shape.get_area() for shape in self.shapes]
        return sum(list_of_area_shapes)
# #==========================================6==============================================#

    def save_to_json(self):
        """
        docstring
        :return:
        """
        with open("shapes.json", "w") as file:
            json.dump([shape.to_dict() for shape in self.shapes], file, indent=4)

# #==========================================7==============================================#

    def load_from_json(self):
        """
        docstring
        :return:
        """
        if os.path.isfile("shapes.json") and os.path.getsize("shapes.json") > 0:
            with open("shapes.json", "r") as file:
                list_of_dicts_of_shapes=list(json.load(file))
            classes = {"square": Square, "rectangle": Rectangle, "circle": Circle}
            for shape in list_of_dicts_of_shapes:
                the_type = shape["type"]
                self.shapes.append(classes[the_type](shape["id"], shape))
                # if shape["type"]=="square":
                #     self.shapes.append(Square(shape["id"], shape["length"]))
                # elif shape["type"]=="rectangle":
                #     self.shapes.append(Rectangle(shape["id"], shape["length"],shape["width"]))
                # elif shape["type"]=="circle":
                #     self.shapes.append(Circle(shape["id"], shape["radius"]))


    def return_object_by_id(self, shape_id):
        for index, shape in enumerate(self.shapes):
            if shape.shape_id == shape_id:
                return shape,index
        return None


    def return_id(self):
        """
        עוברת על המילונים שברשימה ומחפשת את הID הכי גבוה
        :return:
        את הID הכי גבוה+1 לצורך יצירת אובייקט חדש עם ID ייחודי
        """
        correct_id=0
        if not self.shapes:
            return 1
        for shape in self.shapes:
            if shape.shape_id>correct_id:
                correct_id = shape.shape_id
        return correct_id+1
