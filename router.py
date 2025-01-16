from fastapi import APIRouter
from fastapi import FastAPI, Request

app = FastAPI()

router = APIRouter()

app.include_router(router)

@app.get('/')
async def home() -> dict:
    return {'home': 'casa'}

@router.get('/saludos')
async def saludos() -> dict:
    return {'message' : 'Hola a todos'}