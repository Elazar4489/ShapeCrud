import os.path
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
        return shape.to_dict()

#==========================================3==============================================#

    def get_all_shapes(self):
        """
        docstring
        מציגה את כל הצורות (האובייקטים) שקיימות ברשימה
        :return: את הרשימה
        """
        return self.shapes

#==========================================4==============================================#

    def update_shape(self, shape_id: str):
        """
        docstring
        תפקידה ליצור צורה חדשה
        :param shape_id: מקבלת מספר מזהה ייחודי (ע"י הפונקצייה למעלה)
        :return:
        """
        index=0
        update={}
        for shape in self.shapes:
            id4=int(shape["id"])
            if id4==shape_id:
                index=self.shapes.index(shape)
                update=self.check_update_input(shape)
                self.shapes[index] = update
                break
        if len(update)==0:
            print("The shape id does not exist")
            return None

        self.save_to_json()
        return (update)


#==========================================5==============================================#

    def delete_shape(self, shape_id):
        """
        docstring
        :param shape_id:
        :return:
        """
        try:
            the_shape = None
            for shape in self.shapes:
                if shape["id"] == shape_id:
                    the_shape = shape
                    break
            self.shapes.remove(the_shape)
        except ValueError:
            print("invalid value ")
        self.save_to_json()

#==========================================6==============================================#

    def save_to_json(self):
        """
        docstring
        :return:
        """
        with open("shapes.json", "w") as file:
            json.dump(self.shapes, file, indent=4)

#==========================================7==============================================#

    def load_from_json(self):
        """
        docstring
        :return:
        """
        if os.path.isfile("shapes.json") and os.path.getsize("shapes.json") > 0:
            with open("shapes.json", "r") as file:
                self.shapes=list(json.load(file))







    def return_id(self):
        """
        עוברת על המילונים שברשימה ומחפשת את הID הכי גבוה
        :return:
        את הID הכי גבוה+1 לצורך יצירת אובייקט חדש עם ID ייחודי
        """
        id1=0
        if not self.shapes:
            return 1
        for shape in self.shapes:
            if int(shape["id"])>id1:
                id1 = int(shape["id"])
        return id1+1

    def check_choice(self,num, id3):
        if num == "1":
            leni = int(user_input("enter the rid length: "))
            return self.create_square(id3, str(leni))
        if num == "2":
            leni = int(user_input("enter the length: "))
            widi = int(user_input("enter the width: "))
            return self.create_rectangle(id3, str(leni), str(widi))
        if num == "3":
            radi = int(user_input("enter the radius: "))
            return self.create_circle(id3, str(radi))
        print("The shape does not exist in the system")
        return None

    def create_square(self,s_id, rid_length):
        return Square(s_id, rid_length)

    def create_rectangle(self,s_id, length, width):
        return Rectangle(s_id, length, width)

    def create_circle(self,s_id, radius):
        return Circle(s_id, radius)

    def check_update_input(self,the_shape):
        if the_shape["type"] == "square":
            the_shape["length"] = int(user_input("enter the new length: "))

        if the_shape["type"] == "rectangle":
            size = user_input("enter 1 to update the length and 2 to update the width: ")
            if size == "1":
                the_shape["length"] = int(user_input("enter the new length: "))
            if size == "2":
                the_shape["width"] = int(user_input("enter the new width: "))
        if the_shape["type"] == "circle":
            the_shape["radius"] = int(user_input("enter the new radius: "))
        return the_shape
