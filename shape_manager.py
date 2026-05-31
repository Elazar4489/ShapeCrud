import os.path
from shape import Shape
from square import Square
from rectangle import Rectangle
from circle import Circle
from utils import user_input
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

    def create_shape(self, shape, shape_id):
        """
        docstring
        :param shape:
        :return:
        """
        shape = self.check_choice(shape, shape_id)
        return shape

#==========================================3==============================================#

    def get_all_shapes(self):
        """
        docstring
        מציגה את כל הצורות (האובייקטים) שקיימות ברשימה
        :return: את הרשימה
        """
        return [shape.to_dict() for shape in self.shapes]



#==========================================4==============================================#

    def update_shape(self, shape_id):
        """
        docstring
        תפקידה ליצור צורה חדשה
        :param shape_id: מקבלת מספר מזהה ייחודי (ע"י הפונקצייה למעלה)
        :return:
        """
        obj = self.return_object_by_id(shape_id)
        if not obj:
            return None
        dict_of_type_objs={"square": "1", "rectangle": "2", "circle": "3"}
        update=self.create_shape(dict_of_type_objs[obj.shape_type],shape_id)
        self.shapes[self.shapes.index(obj)]=update
        return "The shape updated"


#==========================================5==============================================#

    def delete_shape(self, shape_id):
        """
        docstring
        :param shape_id:
        :return:
        """
        the_shape=self.return_object_by_id(shape_id)
        if the_shape:
            self.shapes.remove(the_shape)

#==========================================6==============================================#

    def save_to_json(self):
        """
        docstring
        :return:
        """
        with open("shapes.json", "w") as file:
            json.dump([shape.to_dict() for shape in self.shapes], file, indent=4)

#==========================================7==============================================#

    def load_from_json(self):
        """
        docstring
        :return:
        """
        if os.path.isfile("shapes.json") and os.path.getsize("shapes.json") > 0:
            with open("shapes.json", "r") as file:
                list_of_dicts_of_shapes=list(json.load(file))
            for shape in list_of_dicts_of_shapes:
                if shape["type"]=="square":
                    self.shapes.append(Square(shape["id"], shape["length"]))
                elif shape["type"]=="rectangle":
                    self.shapes.append(Rectangle(shape["id"], shape["length"],shape["width"]))
                elif shape["type"]=="circle":
                    self.shapes.append(Circle(shape["id"], shape["radius"]))



#==========================================7==============================================#
#==========================================7==============================================#
#==========================================7==============================================#


    def return_object_by_id(self, id_input) -> Shape | None:

        try:
            the_shape = None
            for shape in self.shapes:
                if shape.shape_id == id_input:
                    the_shape = shape
                    break
            return the_shape
        except (ValueError, TypeError):
            print("invalid value ")
            return None
#==========================================7==============================================#

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

#==========================================7==============================================#

    def check_choice(self, num, shape_id):
        if num == "1":
            length = int(user_input("enter the rid length: "))
            return self.create_square(shape_id, length)
        if num == "2":
            length = int(user_input("enter the length: "))
            width= int(user_input("enter the width: "))
            return self.create_rectangle(shape_id, length, width)
        if num == "3":
            radius = int(user_input("enter the radius: "))
            return self.create_circle(shape_id, radius)
        print("The shape does not exist in the system")
        return None

#==========================================7==============================================#

    def create_square(self, shape_id, rid_length):
        return Square(shape_id, rid_length)

#==========================================7==============================================#

    def create_rectangle(self, shape_id, length, width):
        return Rectangle(shape_id, length, width)

#==========================================7==============================================#

    def create_circle(self, shape_id, radius):
        return Circle(shape_id, radius)
