from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo fue agregado exitosamente'}

@todo_router.get('/todo')
async def retrieve_todos() -> dict:
    return {'todos': todo_list}

@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(..., title="El ID de el todo a recuperar")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo con ID indicado no existe."
    }
    
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID de el todo para actualizar")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo actualizado exitosamente"
            }
            return{
                "message": "No existe Todo con ID indicado"
            }
            
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo de ID indicado fue borrado"
            }
            return {
                "message": "No existe Todo con ID indicado"
            }
            
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos fueron borrados exitosamente"
    }