from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
async def read_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
async def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID does not exist")

    del db.data[id]

@app.post("/sheep/{id}", response_model=Sheep, status_code=status.HTTP_201_CREATED)
async def update_sheep(id: int, sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID does not exist")

    db.data[id] = sheep
    return sheep

@app.get("/sheep/", status_code=status.HTTP_200_OK)
async def read_sheeps():
    sheep_list = []
    for sheep in db.data.values():
        sheep_list.append(sheep)
    return sheep_list