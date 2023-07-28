from pydantic import BaseModel

class Todo(BaseModel):
    todo: str
    
class User(BaseModel):
    name: str
    email: str
    password: str