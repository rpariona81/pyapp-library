from fastapi import FastAPI, Request
from todo import todo_router

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {
        'message': 'Hola mundo'
    }

app.include_router(todo_router)