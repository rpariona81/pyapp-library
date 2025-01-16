from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str

#class Todo(BaseModel):
#    id: int
#    item: Item

class Todo(BaseModel):
    id: int
    item: str
    
    class Config:
        json_schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

class TodoItem(BaseModel):
    item: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "item": "Lee el siguiente capítulo de el libro."
            }
        }