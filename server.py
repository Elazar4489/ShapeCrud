from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager, logger

app=FastAPI()
manager=ShapeManager()
@app.get("/shapes")
def return_all_shapes():
    logger.info("A request to display all shapes has been received.")
    try:
        data = manager.get_all_shapes()
        return data
    except HTTPException as e:
        return {"message": f' thw error is{e}'}

@app.get("/shapes/total-area")
def sum_of_all_shape_area():
    logger.info("A request has been received to return the sum of all areas of all shapes.")
    try:
        return manager.get_sum_area()
    except HTTPException as e:
        return {"message": f' thw error is{e}'}


@app.get("/shapes/{shape_id}")
def return_one_shape_by_id(shape_id: int)-> dict:
    if check_id_if_exist(shape_id):
        logger.info(f"Request to display shape number {shape_id} has been received.")
        return manager.get_one_shape(shape_id)
    logger.error(f"Request to display shape number {shape_id} was rejected because the shape does not exist.")
    raise HTTPException(status_code=404, detail=f"shape id {shape_id} not found.")


@app.post("/shapes")
def create_a_new_shape(shape: dict):
    try:
        new_shape=manager.create_shape(shape)
        manager.save_to_json()
        logger.info(f"A {new_shape.shape_type} has been successfully added, and its number is {new_shape.shape_id}.")
        return new_shape.to_dict()
    except KeyError:
        logger.error(f"An attempt to create a shape failed due to corrupt data.")
        raise HTTPException(status_code=400, detail=f"json keys are invalid")
    except ValueError:
        logger.error("An attempt to create a shape failed due to incorrect data types.")
        raise HTTPException(status_code=422, detail=f"parameters shape must be integer")


@app.put("/shapes/{shape_id}")
def replace_a_data_of_shape(shape_id: int, new_data: dict):
    if check_id_if_exist(shape_id):
        try:
            update=manager.update_shape(shape_id,new_data)
            manager.save_to_json()
            logger.info(f"{update.shape_type} update number {update.shape_id} passed successfully.")
            return update.to_dict()
        except KeyError:
            logger.error(f"An attempt to update a shape failed due to corrupt data.")
            raise HTTPException(status_code=400, detail=f"json keys are invalid")
        except ValueError:
            logger.error("An attempt to update a shape failed due to incorrect data types.")
            raise HTTPException(status_code=422, detail=f"parameters shape must be integer")
    logger.error(f"{shape_id}")
    raise HTTPException(status_code=404, detail="the shape is not exist")


@app.delete("/shapes/{shape_id}")
def delete_a_shape(shape_id: int):
    if check_id_if_exist(shape_id):
        shape_deleted=manager.delete_shape(shape_id)
        manager.save_to_json()
        logger.warning(f"Shape number {shape_id} deleted successfully")
        return shape_deleted
    logger.error(f"Deleting shape number {shape_id} failed because the shape is not found.")
    raise HTTPException(status_code=404, detail="shape not found")

def check_id_if_exist(shape_id):
    for shape in manager.shapes:
        if shape.shape_id == shape_id:
            return True
    return False

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)
