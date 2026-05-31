#==========================================7==============================================#

    # def check_update_input(self,the_shape):
    #     if the_shape["type"] == "square":
    #         the_shape["length"] = int(user_input("enter the new length: "))
    #
    #     if the_shape["type"] == "rectangle":
    #         size = user_input("enter 1 to update the length and 2 to update the width: ")
    #         if size == "1":
    #             the_shape["length"] = int(user_input("enter the new length: "))
    #         if size == "2":
    #             the_shape["width"] = int(user_input("enter the new width: "))
    #     if the_shape["type"] == "circle":
    #         the_shape["radius"] = int(user_input("enter the new radius: "))
    #     return the_shape

# def return_dict_by_id(self, id_input) -> dict | None:
#
#     try:
#         the_shape = None
#         for shape in self.shapes:
#             if shape.shape_id == id_input:
#                 the_shape = shape.to_dict()
#                 break
#         return the_shape
#     except (ValueError, TypeError):
#         print("invalid value ")
#         return None
# the_type=""
# for k, v in dict_of_type_objs.items():
#     if obj.shape_type == k:
#         the_type=v