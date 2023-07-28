# imports
from fastapi import FastAPI
from pymongo import MongoClient
import os
import uvicorn
import json
from schema import Todo,User

app = FastAPI()

# declarations
dbv = os.environ.get("MONG_URI")
# connecting mongo
client = MongoClient(dbv)
# connecting db
database = client.Flask
# connecting collection
db = database["Flask_USERS"]


@app.get("/")
async def root():
    return {"message": "hello world!!"}


@app.get("/todos")
def get_todos(todo: Todo):
    return db.find({"todo": todo})


@app.post("/addtodo")
def add_todo(task: Todo): 
    val = db.create(dict(task))
    return val


@app.get('/{id}}')
def get_todo(id: str):
    print({id})
    return "Query parameter.."

# @app.post('/addtodo/save')
# def add_todo_save(todo: Todo):
#     val = db.add(dict(todo))
#     val.save()
#     return val


@app.get("/todo/{item_id}")
def read_item(item_id: str):
    return {"id": item_id}


@app.delete('/del/{item_id}')
def del_by_id(item_id: str):
    try:
        data = db.find_one_and_delete({"item_id": item_id})
    except:
        print('err')    
    print(data)
    
    
@app.get('/test/{task}')
def test(task: str):
    return {"task": task}


@app.get('/todo/{id}')
def get_todo(id: str):
    data = db.find_one_by_id({"id": id})
    return {"data": data}


if __name__ == "__main__":
    uvicorn.run("main:app", port=6969, reload=True)