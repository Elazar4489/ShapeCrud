from shape_manager import ShapeManager, logger
from utils import user_input

"""
main menu - printing the menu, selecting the user and making their selection by sending it to correct function
"""


def main():
    """
    docstring
    :return:
    """
    shape_manager1 = ShapeManager()
    # logger.info(f"System initialized. Loaded {len(shape_manager1.shapes)} shapes from file.")

    flag=True
    while flag:
        print("===MENU===\n"
              "1. Add shape\n"
              "2. Show all shapes\n"
              "3. Update shape\n"
              "4. Delete shape\n"
              "5. Exit")
        user_choice=user_input("Please enter your choice: ")

        try:
            if user_choice == "1":
                print("1. square\n"
                      "2. rectangle\n"
                      "3. circle")
                idd = shape_manager1.return_id()
                the_shape = shape_manager1.create_shape(user_input("choos a shape: "), idd)
                if the_shape:
                    shape_manager1.shapes.append(the_shape)
                # logger.info(f"Successfully created a new {the_shape["type"]} with ID: {the_shape["id"]}.")

            elif user_choice == "3":
                shape_updated=shape_manager1.update_shape(int(user_input("enter the shape id: ")))
                if not shape_updated:
                    print("invalid")

                # logger.warning(f"Shape ID {shape_updated["id"]} was successfully updated.")


            elif user_choice == "4":
                shape_id=int(user_input("enter the shape id: "))
                shape_manager1.delete_shape(shape_id)
                # logger.warning(f"Shape ID {shape_id} has been permanently deleted from the system.")



            elif user_choice == "2":
                print(shape_manager1.get_all_shapes())
                # logger.debug("All shapes requested. Displaying current shape registry.")

            elif user_choice == "5":
                shape_manager1.save_to_json()
                flag= False
                # logger.info(f"Application shutting down. All shape data successfully saved to JSON file.")

            else:
                print("invalid choice!!!\n"
                      "try again\n ")

        except (AttributeError, ValueError):
            print("invalid data")


if __name__=="__main__":
    main()
