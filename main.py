# imports
from fastapi import FastAPI
from pydantic import BaseModel
# from pymongo.mongo.client import MongoClient
from dotenv import *
import os
import uvicorn

app = FastAPI()
# declarations
db = os.environ.get("MONG_URI")

@app.get("/")
async def root():
    db = os.environ.get("BRUHH")
    print(db) 
       
@app.get("/todos")
def get_todos():
    return {"todos": {"id1": "todo1", "id2": "todo2"}}

class Todo(BaseModel):
    todo: str
    id: int
    


if __name__ == "__main__":
    uvicorn.run("main:app", port = 6969, reload = True)