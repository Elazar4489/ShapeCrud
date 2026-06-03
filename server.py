from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager, logger

app=FastAPI()
manager=ShapeManager()
@app.get("/shapes")
def return_all_shapes():
    return manager.get_all_shapes()

@app.get("/shapes/total-area")
def sum_of_all_shape_area():
    sumi=manager.get_sum_area()
    return {"sum area": sumi}


@app.get("/shapes/{shape_id}")
def return_one_shape_by_id(shape_id: int)-> dict:
    try:
        return manager.get_one_shape(shape_id)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"shape id {shape_id} not found.")


@app.post("/shapes")
def create_a_new_shape(shape: dict):
    try:
        new_shape=manager.create_shape(shape)
        manager.save_to_json()
        # logger.info(f"Successfully created a new {new_shape["type"]} with ID: {new_shape["id"]}.")
        return new_shape.to_dict()
    except KeyError:
        # logger.error(f"")
        raise HTTPException(status_code=400, detail=f"shape: {shape} is illegal")


@app.put("/shapes/{shape_id}")
def replace_a_data_of_shape(shape_id: int, new_data: dict):
    try:
        update=manager.update_shape(shape_id,new_data)
        manager.save_to_json()
        return update.to_dict()
    except KeyError:
        raise HTTPException(status_code=400, detail="shape not found")
    except ValueError:
        raise HTTPException(status_code=404, detail="shape parameters are not exist")


@app.delete("/shapes/{shape_id}")
def delete_a_shape(shape_id: int):
    try:
        shape_deleted=manager.delete_shape(shape_id)
        manager.save_to_json()
        return shape_deleted
    except KeyError:
        raise HTTPException(status_code=404, detail="shape not found")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)
